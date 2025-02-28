#!/usr/bin/env python
"""
Test external executable for Binary search.

By default the executable gets a value to find and array sorted in ascending order.

If an element is found executable should prints an array index starting from zero, or -1 otherwise.

If an array contains duplicates, the index of leftmost element is printed.
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
