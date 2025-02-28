#!/usr/bin/env python
"""
Test external executable for monotonic sequence.

By default the executable gets a sequence of ints to deduce if it is monotonously increasing or decreasing.

External executable prints 1 for monotonic sequence, or 0 otherwise.
"""
import unittest
import algotest


class TestMonotonicSequence(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["count_to_ten", "1 2 3 4 5 6 7 8 9 10", "1"],
        ["countdown", "5 4 3 2 1 0", "1"],
        ["duplicates", "1 1 1 2 2 2 3 3 3", "1"],
        ["army_of_two", "1 2", "1"],
        ["binary", "1 0 1 1 1", "0"],
        ["negative", "-3 -2 -1 0 1 2 3", "1"],
        ["false_fives", "5 5 5 4 5", "0"],
        ["fixed_fives", "5 5 5 4 4", "1"],
        ["sole_zero", "0", "1"]
    ]:
        TestMonotonicSequence.add_test_case(*case)

    unittest.main()