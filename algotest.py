#!/usr/bin/env python
"""
Base module for tests.

Set path to target executable as first command line argument in tests run.

By default the executable gets test cases from standard input.

Set logically true value as second command line argument in tests run to pass test cases as command line arguments for executable.
"""

import os
import sys
import subprocess
import unittest


class AlgoTest(unittest.TestCase):
    ExecPath = None
    UseCmdArgs = None

    def setUp(self):
        if not self.ExecPath:
            raise Exception("path to executable is not set")

        if not os.path.exists(self.ExecPath):
            raise FileNotFoundError("executable does not exist")

        return super().setUp()

    def execute(self, input):
        if self.UseCmdArgs:
            proc_result = None

            try:
                proc_result = subprocess.run(
                    [self.ExecPath, input], capture_output=True, timeout=5, text=True)
            except subprocess.TimeoutExpired:
                raise ChildProcessError("executable timed out")

            return proc_result.stdout.rstrip("\n")
        else:
            proc = subprocess.Popen([self.ExecPath], stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            stdout = None

            try:
                stdout, _ = proc.communicate(input, timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                raise ChildProcessError("executable timed out")

            return stdout.rstrip("\n")

    @classmethod
    def add_test_case(klass, name, input, expect):
        def test_case(self):
            got = self.execute(input)
            self.assertEqual(expect, got)

        setattr(klass, f"test_{name}", test_case)


if len(sys.argv) > 1:
    print(sys.argv)
    AlgoTest.ExecPath = sys.argv[1]

    if len(sys.argv) > 2:
        AlgoTest.UseCmdArgs = 1

    # Do not 'irritate' further unittest's command line arguments parsing
    del (sys.argv[1:])
