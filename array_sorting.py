#!/usr/bin/env python
"""
Test external executable for array sorting.

Path to the executable is set via environment variable TESTEXEC.

By default the executable should get an array via command line arguments.

If the executable gets array from standard input one should set environment variable USESTDIN.
"""
import os
import subprocess
import unittest


class TestArraySorting(unittest.TestCase):
    """
    Class for testing external executable for array sorting.
    """

    def setUp(self, test_exec_key="TESTEXEC"):

        if test_exec_key not in os.environ:
            raise KeyError("TESTEXEC is not found in environment variables")

        self.test_exec = os.environ[test_exec_key]

        if not os.path.exists(self.test_exec):
            raise FileNotFoundError("TESTEXEC file does not exist")

    def execute(self, array, use_stdin_key="USESTDIN"):

        if use_stdin_key in os.environ and os.environ[use_stdin_key]:
            proc = subprocess.Popen([self.test_exec], stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            stdout = None

            try:
                stdout, _ = proc.communicate(
                    " ".join(str(i) for i in array), timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                raise ChildProcessError("executable timed out")

            return stdout
        else:
            proc_result = None

            try:
                proc_result = subprocess.run(
                    [self.test_exec, *(str(i) for i in array)], capture_output=True, timeout=5, text=True)
            except subprocess.TimeoutExpired:
                raise ChildProcessError("executable timed out")

            return proc_result.stdout


def generate_test_case(array, expect):
    def test_case(self):
        got = [int(i) for i in self.execute(array).split()]
        self.assertListEqual(expect, got)

    return test_case


if __name__ == "__main__":
    cases = [
        ["zero", [0], [0]],
        ["one", [1], [1]],
        ["zeroes", [0, 0, 0], [0, 0, 0]],
        ["ones", [1, 1, 1], [1, 1, 1]],
        ["one_zero", [1, 0], [0, 1]],
        ["jbond", [0, 7, 0], [0, 0, 7]],
        ["negative", [-1], [-1]],
        ["triple_seven", [7, 7, 7], [7, 7, 7]],
        ["negative_positive", [0, -1, 1], [-1, 0, 1]],
        ["mix", [5, 1, -4, 9, 3, -11, 7, 4, 0, -9],
            [-11, -9, -4, 0, 1, 3, 4, 5, 7, 9]],
        ["from_0_to_9", [5, 3, 9, 2, 0, 6, 1, 7, 4, 8],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
        ["simple_numbers", [41, 19, 61, 7, 5, 53, 89, 13, 29, 83],
            [5, 7, 13, 19, 29, 41, 53, 61, 83, 89]],
        ["years", [1570, 536, 1877, 988, 2021, 2012, 2001, 33, 1925, 1435, 1812, 1913, 1901, 1970], [
            33, 536, 988, 1435, 1570, 1812, 1877, 1901, 1913, 1925, 1970, 2001, 2012, 2021]],
        ["banknotes", [20, 2, 100, 5, 10, 1, 50], [1, 2, 5, 10, 20, 50, 100]],
        ["celcius", [33, -1, -50, 10, 0, 15, -30, -5, 37],
            [-50, -30, -5, -1, 0, 10, 15, 33, 37]]
    ]

    for c in cases:
        setattr(TestArraySorting, f"test_array_sorting_{
                c[0]}", generate_test_case(c[1], c[2]))

    unittest.main()
