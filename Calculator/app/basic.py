#! /usr/bin/env python3
# Author: DCameron
# Description: This module defines some Basic Calculator
# Functions.
"""
    Basic Calculator Functions including add, multiply
    and divide.
"""

def add(x, z):
    """ Return SUM of all parameters as a float
    >>> add(4, 3)
    7.0
    >>> add(10, 20)
    30.0
    """
    return float(x+z)

def mul(x, z):
    """ Return PRODUCT of all parameters as a float
    >>> mul(4, 3)
    12.0
    """
    return float(x*z)

def div(x, z):
    """ Return RESULT of x divided by z to 3 decimal places
    >>> div(4, 3)
    1.333
    """
    return round(x/z, 3)

if __name__ == "__main__":
    # Execute ONLY if ran DIRECTLY as a program
    # IGNORE if imported as a module.
    import doctest
    doctest.testmod()
    #main()