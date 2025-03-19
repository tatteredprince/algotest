#!/usr/bin/env python
"""
Test external executable for balanced parentheses sequence.

By default the executable gets a parentheses sequence.
"""
import unittest
import algotest


class TestBalancedParentheses(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["01", "((", "0"],
        ["02", ")))", "0"],
        ["03", "(())()", "1"],
        ["04", "())(", "0"],
        ["05", "()", "1"],
        ["06", "()()", "1"],
        ["07", ")()(", "0"]
    ]:
        TestBalancedParentheses.add_test_case(*case)

    unittest.main()
