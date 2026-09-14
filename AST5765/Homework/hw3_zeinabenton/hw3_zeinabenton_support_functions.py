
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

    

def squareplot(var1, var2, n, saveplot=False) :
    """
    Squareplot is to plot the squares of numbers.

    Works with definition square to plot the squares of numbers.

    Parameters
    ----------
    var1 : array_like
        Low numbers to be squared and plotted.  

    var2 : array_like
        High numbers to be squared and plotted.

    n: int
        Number of points to be plotted.

    Optional Parameters
    ----------
    saveplot : string, optional
        If True, saves the plot as a PDF file. Default is False.
    
    Returns
    -------
    None

    Examples
    -----
    >>> squareplot(5, 10, 100)
    >>> squareplot(5, 10, 100, 'hw3_zeinabenton_squareplot.pdf')
    Plot

    """
    x = np.linspace(var1, var2, n)
    y = square(x)

    plt.plot(x, y)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.title('Square Function')
    if saveplot is not False:
        plt.savefig(saveplot, format='pdf')

    plt.show()


    


