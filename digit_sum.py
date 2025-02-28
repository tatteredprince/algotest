#!/usr/bin/env python
"""
Test external executable for digit sum.

By default the executable gets a number to summarize its digits.
"""
import unittest
import algotest


class TestDigitSum(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["first_five", "12345", "15"],
        ["count_to_ten", "12345678910", "46"],
        ["one_hundred", "100", "1"],
        ["jbond", "007", "7"],
        ["zero", "0", "0"],
        ["binseq", "1011011101", "7"],
    ]:
        TestDigitSum.add_test_case(*case)

    unittest.main()
