#Zeina Benton
#HW5
#9/25/26

def sigrej(data, threshold, mask=None):
    """
    Perform sigma rejection on the input data.
    
    Parameters
    ----------
    data : array-like
        The input data to be filtered.
    threshold : tuple
        Number of standard deviations for rejection at each iteration.
    mask : array-like of bool, optional
        Boolean mask indicating initially good data points.
        True = good, False = bad.
    
    Returns
    -------
    mask : array-like of bool
        Modified Boolean mask after sigma rejection.

    Examples
    --------
    data = np.array([10, 11, 10, 12, 11, 10, 50])
    result = sigrej(data, (2.,))
    print(result)
    >> [ True  True  True  True  True  True False]
    print(data[result])
    >> [10 11 10 12 11 10]

    
    data = np.random.normal(loc=100, scale=10, size=100)
    result = sigrej(data, (2.,))
    print(result)
    >> [ True  True  True  True  True  True  True  True  True  True  True  True
    True  True False  True  True  True  True  True  True  True  True  True
    True  True  True  True  True  True  True  True  True  True  True  True
    True  True  True  True  True  True  True  True False  True  True  True
    True  True  True  True  True  True  True  True  True  True  True  True
    False  True  True  True 
    print(data[result])
    >>> [102.94964571 100.78131676  98.62252774  99.71517574 105.63355767
    112.34002946 103.86869781  88.78916429  89.92768794  96.3139004
    103.81800466  88.26729565  89.44511362  94.17789326  99.78388179
    86.48067531  78.88877032  97.8708369   95.45838359  99.63327367
    105.33887733  97.83207736  97.8668433   92.26161264 106.55112828
    116.84538566  93.99933105  90.02912072  91.77227181  84.11159573
    99.75744773  98.89691697  93.53969808 102.08298867  84.78525959
    98.02316842  87.32705051  97.93742644  86.16755669 106.53466935
    97.29420313 100.32531154 104.82141521 104.34303993 103.56328312
    89.58186128  84.3367037   92.97352427  99.0354064  103.02977604
    98.21056616  87 ... ]

    data = np.random.normal(loc=100, scale=10, size=100)
    result = sigrej(data, (4.,4.))
    print(result)
    >>> [True  True  True  True  True  True  True  True  True  True  True  True
    True  True  True  True  True  True  True  True  True  True  True  True
    True  True  True  True  True  True  True  True  True  True  True  True
    True  True  True  True  True  True...]
    print(data[result])
    >>> [ 81.05636249  99.29255048 101.77127154  93.70921651  97.38301135
    108.65109197  97.06780521  97.84860837  99.188078   112.45383848
    98.32528338  85.93416891 122.31077342 101.54824593 107.83775398
    105.0254307  104.22311965  96.0854888  105.18346834  94.15082564
    99.22003663  83.43975279  91.89630915  89.71147205 110.75345431
    99.61494164  83.97959453 104.14070571 100.19537763  88.81746444
    113.41775385  87.80249939  96.07324685  97.42913944 107.99854395
    109.84873505  99.52962272 102.86211573  95.2265064  113.00531509...]
    
    
    """
    import numpy as np

    data = np.asarray(data)

    if mask is None: #Only use good data points
        mask = np.ones(data.shape, dtype=bool)
    else:
        mask = np.asarray(mask, dtype=bool).copy()

    
    for N in threshold: 
        good_data = data[mask]

        mean = np.mean(good_data)
        std_dev = np.std(good_data)

        mask[np.abs(data - mean) > N * std_dev] = False #flag bad pixels as false

    return mask