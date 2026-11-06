#Zeina Benton
#practicum 5
#10/14/26

#%%
import numpy as np

def normmedcomb(arr, keyword=True, coordinates=None):
    """
    This function implements normalized median combination method.
    
    Parameters
    ----------
    arr : ndarray
        3D array of dark-subtracted sky images.
    keyword : bool, optional
        False: normalize using the whole image.
        True: normalize using the supplied coordinates.
    coordinates : tuple, optional
        Region (y_1, x_1, y_2, x_2), required when keyword=True.

    Returns
    -------
    normmedcomb : 2D array
        Normalized median combination of the input array.
    
    Example
    -------
    >>> arr = np.random.rand(5, 100, 100)  # Example 3D array
    >>> result = normmedcomb(arr, keyword=True, coordinates=(10, 10, 90, 90))

    Note
    -----
    The normalization region is the region from which the normalization factor is calculated in each frame.

    """
    # Check if the input array is 3D
    if arr.ndim != 3:
        raise ValueError("Input array must be 3D.")

    n_frames, height, width = arr.shape

    if keyword is False:
        y_1, x_1, y_2, x_2 = (0, 0, height, width)

    elif keyword is True:
        if coordinates is None:
            raise ValueError("Supply coordinates when keyword=True.")
        y_1, x_1, y_2, x_2 = coordinates

    else:
        raise ValueError("Keyword must be True or False.")

    normalized_frames = np.zeros_like(arr, dtype=float) #Empty array to store normalized frames
    norm_factors = np.zeros(n_frames)

    for i in range(n_frames):
        norm_factors[i] = np.median(arr[i, y_1:y_2, x_1:x_2])

        if not np.isfinite(norm_factors[i]) or norm_factors[i] == 0:
            raise ValueError("Normalization factor must be finite and nonzero.")

        normalized_frames[i] = arr[i] / norm_factors[i]

    combined = np.median(normalized_frames, axis=0)

    return combined, norm_factors