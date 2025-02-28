#!/usr/bin/env python
"""
Test external executable for Fibonacci sequence.

By default the executable gets two numbers and quantity of numbers to calculate.
"""
import unittest
import algotest


class TestFibonacciNumbers(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["next", "0 1 1", "1"],
        ["first_five", "0 1 5", "1 2 3 5 8"],
        ["double_digits", "5 8 5", "13 21 34 55 89"],
        ["triple_digits", "55 89 5", "144 233 377 610 987"],
        ["big_numbers", "832040 1346269 10",
            "2178309 3524578 5702887 9227465 14930352 24157817 39088169 63245986 102334155 165580141"]
    ]:
        TestFibonacciNumbers.add_test_case(*case)

    unittest.main()
