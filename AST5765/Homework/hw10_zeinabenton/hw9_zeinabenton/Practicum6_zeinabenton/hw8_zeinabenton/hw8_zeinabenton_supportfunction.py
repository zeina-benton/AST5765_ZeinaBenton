#Zeina Benton
#HW 8
#10/14/26

#%%
import numpy as np

def skycormednorm(arr_1, arr_2, keyword=None):
    """
    This function implements sky subtraction using your normalized sky frame.
    
    Parameters
    ----------
    arr_1 : ndarray
        2D array of object frame.
    arr_2 : ndarray
        2D of normalized sky frame
    keyword : tuple, optional
        Normalization region: ((y1, x1), (y2, x2)).
        Default: the whole object frame.
  
    Returns
    -------
    skycormednorm : 2D array
        De-normalized the sky, subtract it from the object frame, and returns the resulting sky-subtracted frame.
    
    Example
    -------
    >>> corrected = skycormednorm(arr_1, arr_2)
    >>> corrected = skycormednorm(arr_1, arr_2, keyword=((225, 225), (-225, -225)))
    
    Note
    -----
    Both object frame and sky frame should be already dark-subtracted.

    """
    # Check if the input array is 2D, raise concerns
    if arr_1.ndim != 2 or arr_2.ndim != 2:
        raise ValueError("Both inputs must be 2D.")

    if arr_1.shape != arr_2.shape:
        raise ValueError("Both inputs must have the same shape.")


    if keyword is None: 
        region = arr_1 #Background level of the object frame to scale the normalized sky
    else:
        (y1, x1), (y2, x2) = keyword
        region = arr_1[y1:y2, x1:x2]


    if region.size == 0: #Check region
        raise ValueError("Normalization region is empty.")

    norm_factor = np.median(region)

    if not np.isfinite(norm_factor): #Check
        raise ValueError("Normalization factor must be finite.")

    denormalized_sky = arr_2 * norm_factor #Apply normalization factor
    corrected = arr_1 - denormalized_sky 

    return corrected