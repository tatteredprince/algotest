#!/usr/bin/env python
"""
Test external executable for array sorting.

Path to the executable is set via environment variable TESTEXEC.

By default the executable should get an array via command line arguments.

If the executable gets array from standard input one should set environment variable USESTDIN.
"""
import unittest
import algotest


class TestArraySorting(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["zero", "0", "0"],
        ["one", "1", "1"],
        ["zeroes", "0 0 0", "0 0 0"],
        ["ones", "1 1 1", "1 1 1"],
        ["one_zero", "1 0", "0 1"],
        ["jbond", "0 7 0", "0 0 7"],
        ["negative", "-1", "-1"],
        ["triple_seven", "7 7 7", "7 7 7"],
        ["negative_positive", "0 -1 1", "-1 0 1"],
        ["mix", "5 1 -4 9 3 -11 7 4 0 -9",
            "-11 -9 -4 0 1 3 4 5 7 9"],
        ["from_0_to_9", "5 3 9 2 0 6 1 7 4 8",
            "0 1 2 3 4 5 6 7 8 9"],
        ["simple_numbers", "41 19 61 7 5 53 89 13 29 83",
            "5 7 13 19 29 41 53 61 83 89"],
        ["years", "1570 536 1877 988 2021 2012 2001 33 1925 1435 1812 1913 1901 1970",
            "33 536 988 1435 1570 1812 1877 1901 1913 1925 1970 2001 2012 2021"],
        ["banknotes", "20 2 100 5 10 1 50", "1 2 5 10 20 50 100"],
        ["celcius", "33 -1 -50 10 0 15 -30 -5 37",
            "-50 -30 -5 -1 0 10 15 33 37"],
    ]:
        TestArraySorting.add_test_case(*case)

    unittest.main()
