#!/usr/bin/env python
"""
Test external executable for balanced brackets sequence.

By default the executable gets a brackets sequence.
"""
import unittest
import algotest


class TestBalancedBrackets(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["01", "(())()", "1"],
        ["02", "())(", "0"],
        ["03", "[{()}]", "1"],
        ["04", "[()()]{}", "1"],
        ["05", "([]", "0"],
        ["06", "([{]})", "0"],
        ["07", "()", "1"],
        ["08", "()[]{}", "1"],
        ["09", "(]", "0"],
        ["10", "([])", "1"]
    ]:
        TestBalancedBrackets.add_test_case(*case)

    unittest.main()
