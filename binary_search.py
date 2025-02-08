#!/usr/bin/env python
"""
Test external executable for Binary search.

Path to the executable is set via environment variable TESTEXEC.

By default the executable gets a value to find and array sorted in ascending order via command line arguments.

Executable should return index starting from zero for found element or -1.

If array contains duplicates, then index of leftmost elements should be printed.

If the executable gets input from standard input one should set environment variable USESTDIN.
"""
import unittest
import algotest


class TestBinarySearch(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["found", "6 0 1 2 3 4 5 6 7 8 9", "6"],
        ["not_found", "11 0 1 2 3 4 5 6 7 8 9", "-1"],
        ["found_in_duplicate", "4 0 1 2 3 4 4 4 5 6 7 8 9", "4"],
        ["not_found_in_duplicate", "11 0 1 2 3 4 4 4 5 6 7 8 9", "-1"],
        ["zero_array", "11", "-1"]
    ]:
        TestBinarySearch.add_test_case(*case)

    unittest.main()
