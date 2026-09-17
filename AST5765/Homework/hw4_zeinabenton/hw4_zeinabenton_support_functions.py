#Zeina Benton
#HW4
#9/17/26


import numpy as np

#2a
def gaussian_random_generator(N, mu, sigma):
    """
    Generates N random numbers from a Gaussian distribution with mean mu and standard deviation sigma.

    Parameters
    ----------
    N : int
        The number of random numbers to generate.
    mu : float
        The mean of the Gaussian distribution.
    sigma : float
        The standard deviation of the Gaussian distribution.
    Returns
    -------
    random_numbers : array_like
        An array of N random numbers drawn from the specified Gaussian distribution.

    Examples
    -----
    >>> print(gaussian_random_generator(5, 0, 1))
    [ 0.49671415 -0.1382643   0.64768854  1.52302986 -0.23415337]
    >>> print(gaussian_random_generator(3, 10, 2))
    [ 9.76405235 11.16420955  8.14294754]

    """ 
    return np.random.normal(mu, sigma, N)

#2c
def gaussian(x, mu, sigma):
    """
    Calculates the Gaussian probability density at each point in N.


    Parameters
    ----------
    x : array_like
        All objects -- lists, nested lists, etc. --
        that can be converted to an array.  
    mu : float
        The mean of the Gaussian distribution.
    sigma : float
        The standard deviation of the Gaussian distribution.
    

    Returns
    -------
    p_x : array_like
        The gaussian probability density at each point in N.

    Examples
    -----
    >>> print(gaussian(5, 0, 1))
    0.3989422804014327

    >>> print(gaussian(np.array([1,2,3]), 0, 1))
    [0.24197072 0.05399097 0.00443185]

    """
    variables = (1/(sigma * np.sqrt(2 * np.pi)))
    exp =  np.exp(-0.5 * ((x - mu) / sigma)**2)
    p_x = variables * exp

    return p_x


#3a
def fwhm(sigma):
    """
    Calculates the full width at half maximum (FWHM) of a Gaussian distribution.

    -----
    Parameters
    ----------
    sigma : float
        The standard deviation of the Gaussian distribution.
    Returns
    -------
    fwhm_value : float
        The full width at half maximum (FWHM) of the Gaussian distribution.
    Examples
    -----
    >>> print(fwhm(1))
    2.3548200450309493

    >>> print(fwhm(2))
    4.7096400900618985

    Notes
    -----
    Derivation:

    p(x) = A * exp[-0.5 * ((x - mu)/sigma)^2]

    A/2 = A * exp[-0.5 * ((x - mu)/sigma)^2]

    1/2 = exp[-0.5 * ((x - mu)/sigma)^2]

    ln(1/2) = -0.5 * ((x - mu)/sigma)^2

    ln(2) = 0.5 * ((x - mu)/sigma)^2

    2 * ln(2) = ((x - mu)/sigma)^2

    sqrt(2 * ln(2)) = (x - mu)/sigma

    x - mu = sigma * sqrt(2 * ln(2))

    mu - sigma*sqrt(2ln(2))
    mu + sigma*sqrt(2ln(2))

    Therefore:
    FWHM = 2*sigma*sqrt(2ln(2))

    """
    fwhm_value = 2 * np.sqrt(2 * np.log(2)) * sigma
    return fwhm_value

