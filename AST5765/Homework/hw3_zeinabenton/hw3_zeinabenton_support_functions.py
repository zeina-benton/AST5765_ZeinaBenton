hw3_zeinabenton_support_functions.py

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
from my_module import my_func, other_func
#then write your functions


def square(var1, var2, long_var_name='hi') :
    """
    square takes as input a scalar or array of any dimension or numerical type and
    returns its square.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    Long_variable_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    describe : type
        Explanation
    output : type
        Explanation
    tuple : type
        Explanation
    items : type
        even more explaining

    Other Parameters
    ----------------
    only_seldom_used_keywords : type
        Explanation
    common_parameters_listed_above : type
        Explanation

    Raises
    ------
    BadException
        Because you shouldn't have done that.

    See Also
    --------
    otherfunc : relationship (optional)
    newfunc : Relationship (optional), which could be fairly long, in which
              case the line wraps here.
    thirdfunc, fourthfunc, fifthfunc

    Notes
    -----
    Notes about the implementation algorithm (if needed).

    This can have multiple paragraphs.

    You may include some math:

    .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

    And even use a greek symbol like :math:`omega` inline.

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.  Use the plain python prompt (">>> ") for the
    example commands, and put the expected output on a line without a
    prompt, as follows:


    >>> a=[1,2,3]
    >>> print([x + 3 for x in a])
    [4, 5, 6]
    >>> print("a\n\nb")
    a
    <BLANKLINE>
    b

    The examples in docstrings can be run with the 'doctest' package:

    python -m doctest -v doctest_simple_with_docs.py

    See:

    https://pymotw.com/2/doctest/

    for more examples.  There are several different testing packages,
    including 'doctest' and 'nose'.  All use the same format when it
    comes to tests in docstrings, but offer different testing
    functionality.

    nosetests --with-doctest your_python_file.py

    If your example prints random numbers, use an ellipsis ('...') to
    skip the part of the output that is variable.

    Revisions
    ---------
    2008-09-11 jh@physics.ucf.edu added Revisions section
               The Revisions section is where you record modifications
               to the file.  In the Python and NumPy sources, this is
               handled by a revision control system like Git.  If you
               are not using one, and even sometimes if you are, it's
               good to put the revision notes right into the
               docstring.

    2008-09-11 jh@physics.ucf.edu downloaded and edited from
        http://projects.scipy.org/scipy/numpy/browser/trunk/doc/example.py
    2014-08-26 jh@physics.ucf.edu updated docstring
    2016-09-14 jh@physics.ucf.edu Added doctest commands and discussion.
    2018-08-30 jh@physics.ucf.edu updated original from
    https://github.com/andyk/load_gen/blob/master/numpy/doc/example.py
        and merged local changes.
    """

#this is the main body of your function

#remember your code should be well-commented throughout!

    pass

