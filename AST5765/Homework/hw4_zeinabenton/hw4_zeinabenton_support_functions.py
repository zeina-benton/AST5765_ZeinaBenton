import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt  # NOTE: pyplot, *not* pylab!
import astropy.io.fits as fits

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

