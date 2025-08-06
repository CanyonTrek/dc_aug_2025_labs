#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""

# import app.basic
from app import basic

def main():
    print("******** Basic Calc App *********")
    print(f"4 + 3 = {basic.add(4, 3)}")
    print(f"4 * 3 = {basic.mul(4, 3)}")
    print(f"4 / 3 = {basic.div(4, 3)}")
    print("**********************************")
    return None

if __name__ == "__main__":
    # Execute ONLY if ran DIRECTLY as a program
    # IGNORE if imported as a module.
    import doctest
    doctest.testmod()
    main()