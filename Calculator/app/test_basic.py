#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import sys
# import basic
from basic import add, mul, div

def test_add():
    assert add(4, 3) == 7.1, "Should be 7.1"
    assert add(10, 20) == 30.0, "Should be 30.0"
    return None

def test_mul():
    assert mul(4, 3) == 12.1, "Should be 12.1"
    assert mul(4, 5) == 20.0, "Should be 20.0"
    return None

def test_div():
    assert div(4, 3) == 1.334, "Should be 1.334"
    return None

def main():
    print("Starting Tests..")
    try:
        test_add()
    except AssertionError as err:
        print(f"Found Error, {err}", file=sys.stderr)
    test_mul()
    test_div()
    print("All tests SUCCESSFUL")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran DIRECTLY as a program
    # but ignored if imported as a module.
    main()
