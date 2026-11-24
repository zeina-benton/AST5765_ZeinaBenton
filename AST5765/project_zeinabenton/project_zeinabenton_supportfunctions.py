#Zeina Benton
#Final Project Support Functions
#11/23/26

#%%
from scipy.interpolate import CubicSpline #Splines to evaluate a spectrum
import gaussian as g

def splinterp(xnew, xold, yold):
    """
    Evaluate a cubic spline through the original data at xnew.

    Parameters
    ----------
    xnew : array_like
        The x-coordinates at which to evaluate the spline.
    xold : array_like
        The x-coordinates of the original data points.
    yold : array_like
        The y-coordinates of the original data points.
    
    Returns
    -------
    array_like
        The y-coordinates of the spline evaluated at xnew.
    
    Example
    -------
    >>> xold = np.array([-2.0, -1.0, 0.0, 1.0, 2.0])
    >>> yold = np.array([0.1353, 0.6065, 1.0, 0.6065, 0.1353])
    >>> xnew = np.array([-1.5, -0.5, 0.5, 1.5])
    >>> splinterp(xnew, xold, yold)
    array([0.3247, 0.7788, 0.7788, 0.3247])
    
    """
    
    spline = CubicSpline(xold, yold, extrapolate=True)
    return spline(xnew)


from scipy.signal import correlate, correlation_lags # Handles signal processing, built in scipy
import numpy as np

def interp_xcorr(spectrum, reference, oversample=10, max_lag=None,
                 peak_half_window=5):
    """
    Return the offset of spectrum relative to reference in original pixels.
    
    Parameters
    ----------
    spectrum : array_like
        The spectrum to be shifted.
    reference : array_like
        The reference spectrum.
    oversample : int, optional
        The oversampling factor for the cross-correlation. Default is 10.
    max_lag : float, optional
        The maximum lag (in pixels) to consider for the cross-correlation.
        If None, all lags are considered. Default is None.
    peak_half_window : int, optional
        The half-width of the window around the peak for Gaussian fitting.
        Default is 5.
    
    Returns
    -------
    float
        The estimated shift of spectrum relative to reference in original pixels.   

    Exmaple
    -------
    >>> spectrum = np.array([0.0, 1.0, 0.0, 0.0])
    >>> reference = np.array([0.0, 0.0, 1.0, 0.0])
    >>> interp_xcorr(spectrum, reference)
    2.0
    
    
    """

    spectrum = np.asarray(spectrum, dtype=float)
    reference = np.asarray(reference, dtype=float)

    # Raising flags for invalid inputs
    if spectrum.ndim != 1 or spectrum.shape != reference.shape:
        raise ValueError("Use two one-dimensional spectra of equal length.")
    if spectrum.size < 4:
        raise ValueError("Each spectrum needs at least four pixels.")
    if not np.all(np.isfinite(spectrum)) or not np.all(np.isfinite(reference)):
        raise ValueError("Both spectra must contain finite values.")
    if np.ptp(spectrum) == 0 or np.ptp(reference) == 0:
        raise ValueError("A constant spectrum cannot determine a shift.")
    if not isinstance(oversample, (int, np.integer)) or oversample < 10:
        raise ValueError("oversample must be an integer of at least 10.")
    if not isinstance(peak_half_window, (int, np.integer)) or peak_half_window < 2:
        raise ValueError("peak_half_window must be an integer of at least 2.")
    if max_lag is not None and (not np.isfinite(max_lag) or max_lag < 0):
        raise ValueError("max_lag must be finite and nonnegative.")

    # Make the original and fine pixel grids.
    xold = np.arange(spectrum.size)
    xfine = np.arange(spectrum.size * oversample) / oversample

    # Interpolate each spectrum once, then subtract its mean
    spectrum_fine = splinterp(xfine, xold, spectrum)
    reference_fine = splinterp(xfine, xold, reference)
    spectrum_fine = spectrum_fine - spectrum_fine.mean()
    reference_fine = reference_fine - reference_fine.mean()

    # Pad both ends with one interpolated spectrum's worth of zeros.
    n_fine = xfine.size
    spectrum_padded = np.pad(spectrum_fine, n_fine)
    reference_padded = np.pad(reference_fine, n_fine)

    # Get the score and offset for each alignment, then convert the offsets to original pixels
    corr = correlate(spectrum_padded, reference_padded, mode="full", method="fft")
    lag_steps = correlation_lags(spectrum_padded.size, reference_padded.size)
    lags = lag_steps / oversample

    # Keep lags with overlapping data and apply the optional search limit
    keep = np.abs(lag_steps) < n_fine
    if max_lag is not None:
        keep &= np.abs(lags) <= max_lag

    lags = lags[keep]
    corr = corr[keep]
    peak = np.argmax(corr)
    grid_shift = lags[peak]
    step = 1.0 / oversample

    # Take best found lag and refine it by fitting a Gaussian to the nearby correlation scores
    for half_window in dict.fromkeys((peak_half_window, 2)):
        if peak < half_window or peak + half_window >= lags.size:
            continue

        region = slice(peak - half_window, peak + half_window + 1)
        fit_lags = lags[region]
        fit_corr = corr[region]
        if corr[peak] <= 0 or np.ptp(fit_corr) == 0:
            continue

        # Gaussian guesses for width, center, height, and errors
        guess = (half_window * step, grid_shift, corr[peak])
        try:
            width, center, height, errors = g.fitgaussian(
                fit_corr, fit_lags, guess=guess
            )
        except (ValueError, TypeError, RuntimeError):
            continue

        # Shift estimated from the center of the fitted Gaussian.
        shift_fit = float(center[0])
        if not np.all(np.isfinite(errors)) or width[0] <= 0 or height <= 0:
            continue

        # Check whether the fit is good with function
        fitted_corr = g.gaussian(fit_lags, width, center, height)
        rms_error = np.sqrt(np.mean((fit_corr - fitted_corr)**2))

        # Accept a nearby center if the fit reproduces the local peak.
        if abs(shift_fit - grid_shift) < step and rms_error < 0.1 * np.ptp(fit_corr):
            return shift_fit
    # Raise flag if the Gaussian fit could not refine the peak, and return the grid shift.
    print(f"Warning: Gaussian fit could not refine the peak. "
          f"Using the grid shift of {grid_shift:+.4f} pixels.")
    return float(grid_shift)