#! /usr/bin/env python3
# Author: DCameron
# Description: This script will demo
"""
    Docstring:
"""
import sys
import unittest
from Calculator.app.basic import add, mul, div
# from app.basic import add, mul, div

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 3), 7.0, "Should be 7.0")
        self.assertEqual(add(10, 20), 30.0, "Should be 30.0")
        return None

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12.0, "Should be 12.0")
        self.assertEqual(mul(4, 5), 20.0, "Should be 20.0")
        return None

    def test_div(self):
        self.assertEqual(div(4, 3), 1.333, "Should be 1.334")
        return None


# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran DIRECTLY as a program
    # but ignored if imported as a module.
    unittest.main()
