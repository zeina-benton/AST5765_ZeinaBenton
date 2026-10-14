#Zeina Benton
#HW 7
#10/8/26

import numpy as np

def box_window(time, center, width, depth):
    """
    This function generates a box transit model whose fitted depth can
    be used to calculate the planetary radius.

    Parameters
    ----------
    time : array-like
        The x  values at which to evaluate the transit model.
    center : float
        The center time of the transit.
    width : float
        The duration of the transit (full width).
    depth : float
        The depth of the transit (fractional decrease in flux).
    
    Returns
    -------
    model_flux : ndarray
        Normalized flux values for the box-shaped transit.

    Notes
    -----
    After fitting, calculate the planetary radius using
    Rp = Rstar * sqrt(depth). For Rstar = 1.14 solar radii,
    Rp = 1.14 * sqrt(depth) in solar radii.

    Examples
    --------
    time = np.linspace(-0.1, 0.1, 100)
    center = 0.0
    width = 0.02
    depth = 0.01
    model_flux = box_window(time, center, width, depth)
    print(model_flux.shape)
    >>> (100,)


    """
    in_transit = np.abs(time - center) <= width / 2 #Calculates whether each time point is within the transit window (True) or outside (False)
    return np.where(in_transit, 1.0 - depth, 1.0) #1.0 because the flux is normalized to 1.0 outside of transit
