
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt  # NOTE: pyplot, *not* pylab!
import astropy.io.fits as fits

# These abbreviated names are not to be used in docstrings; users must
# be able to paste and execute docstrings after importing only the
# numpy module itself, unabbreviated.
#if you need to import functions from other files you can do it
#afterwards like this:
#from my_module import my_func, other_func
#then write your functions


def square(var1) :
    """
    square takes as input a scalar or array of any dimension or numerical type and
    returns its square.

    AKA  square returns the square of its input. 

    Parameters
    ----------
    var1 : array_like
        All objects -- lists, nested lists, etc. --
        that can be converted to an array.  

    Returns
    -------
    Squared : array_like
        The square of the input.

    Examples
    -----
    >>> print(square(5))
    25

    >>> print(square(np.array([1,2,3])))
    [1 4 9]

    """

    squared = var1**2
    return squared

    

