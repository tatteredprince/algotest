#!/usr/bin/env python
"""
Test external executable for Digit sum.

Path to the executable is set via environment variable TESTEXEC.

By default the executable gets a number to summarize its numers via command line arguments.

If the executable gets input from standard input one should set environment variable USESTDIN.
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
