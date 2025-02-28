#!/usr/bin/env python
"""
Test external executable for arab to roman numbers conversion.

By default the executable gets an arab number to print a roman number.
"""
import unittest
import algotest


class TestArab2Roman(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["alphabet_1", "1", "I"],
        ["alphabet_5", "5", "V"],
        ["alphabet_10", "10", "X"],
        ["alphabet_50", "50", "L"],
        ["alphabet_100", "100", "C"],
        ["alphabet_500", "500", "D"],
        ["alphabet_1000", "1000", "M"],
        ["number_39", "39", "XXXIX"],
        ["number_246", "246", "CCXLVI"],
        ["number_789", "789", "DCCLXXXIX"],
        ["number_2421", "2421", "MMCDXXI"],
        ["number_160", "160", "CLX"],
        ["number_207", "207", "CCVII"],
        ["number_1009", "1009", "MIX"],
        ["number_1066", "1066", "MLXVI"],
        ["year_1776", "1776", "MDCCLXXVI"],
        ["year_1918", "1918", "MCMXVIII"],
        ["year_1944", "1944", "MCMXLIV"],
        ["year_2025", "2025", "MMXXV"],
    ]:
        TestArab2Roman.add_test_case(*case)

    unittest.main()
