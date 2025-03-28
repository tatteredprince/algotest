#!/usr/bin/env python
"""
Test external executable for two sum.

By default the executable gets an array and target value.

If a pair of elements whose sum constituents a target value is found then 1 is printed to standard output, or 0 otherwise.
"""
import unittest
import algotest


class TestTwoSum(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["binary_sequence", "0 1 0 1 0 1 2", "1"],
        ["take_two", "0 1 0 1 0 1 3", "0"],
        ["zeroes", "0 0 0 0 0 0 0", "1"],
        ["one_palm", "1 2 3 4 5 8", "1"],
        ["two palms", "1 2 3 4 5 6 7 8 9 10 33", "0"],
    ]:
        TestTwoSum.add_test_case(*case)

    unittest.main()
