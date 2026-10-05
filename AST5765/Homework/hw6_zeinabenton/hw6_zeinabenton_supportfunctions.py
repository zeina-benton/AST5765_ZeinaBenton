#Zeina Benton
#Homework 6
#10/5/26

def median_stack_method(data):
    """
    This function allows you to median-combine the images in
    a single function call, without loops.

    Parameters
    ----------
    data: 3D array of images to be median-combined

    Returns
    -------
    median_combined: 2D array of the median-combined image

    Examples
    --------
    data = np.random.normal(loc=100, scale=10, size=(5, 100, 100))
    median_combined = median_stack_method(data)
    print(median_combined.shape)
    >> (100, 100)

    data = darks # 3D array of dark images
    median_combined = median_stack_method(darks)
    print(median_combined.shape)
    >> (100, 100)

    """
    import numpy as np
    median_combined = np.median(data, axis=0) #Median combine the images along the first axis (the image index)
    return median_combined


    
    
    
    
    
    
    
    
