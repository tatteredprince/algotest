#!/usr/bin/env python
"""
Test external executable for zipping arrays.

Path to the executable is set via environment variable TESTEXEC.

By default the executable gets array of arrays to zip them into one-dimensional array via command line arguments.

If the executable gets input from standard input one should set environment variable USESTDIN.
"""
import unittest
import algotest


class TestZipArrays(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["one_two_three", "[1 1 1] [2 2 2] [3 3 3]", "[1 2 3] [1 2 3] [1 2 3]"],
        ["twins", "[1] [2]", "[1 2]"],
        ["simple", "[1 2] [3]", "[1 3]"],
        ["complex", "[9 8 7 6] [5 4 3] [2 1]", "[9 5 2] [8 4 1]"],
        ["empty_array", "[1 2 3] []", "[]"]
    ]:
        TestZipArrays.add_test_case(*case)

    unittest.main()