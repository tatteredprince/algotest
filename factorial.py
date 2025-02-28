#!/usr/bin/env python
"""
Test external executable for factorial.
"""
import algotest
import unittest


class FactorialTesting(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["zero", "0", "1"], ["one", "1", "1"],
        ["two", "2", "2"], ["three", "3", "6"],
        ["seven", "7", "5040"], ["ten", "10", "3628800"],
        ["twenty", "20", "2432902008176640000"]
    ]:
        FactorialTesting.add_test_case(*case)

    unittest.main()
