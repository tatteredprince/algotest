#!/usr/bin/env python
"""
Base module for tests.

Check environment variables and external executable before starting tests.

Path to the executable is set via environment variable TESTEXEC.

If the executable gets data from standard input one should set environment variable USESTDIN.
"""
import os
import subprocess
import unittest


class AlgoTest(unittest.TestCase):
    def setUp(self, test_exec_key="TESTEXEC"):

        if test_exec_key not in os.environ:
            raise KeyError("TESTEXEC is not found in environment variables")

        self.test_exec = os.environ[test_exec_key]

        if not os.path.exists(self.test_exec):
            raise FileNotFoundError("TESTEXEC file does not exist")

    def execute(self, input, use_stdin_key="USESTDIN"):

        if use_stdin_key in os.environ and os.environ[use_stdin_key]:
            proc = subprocess.Popen([self.test_exec], stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            stdout = None

            try:
                stdout, _ = proc.communicate(input, timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                raise ChildProcessError("executable timed out")

            return stdout.rstrip()
        else:
            proc_result = None

            try:
                proc_result = subprocess.run(
                    [self.test_exec, input], capture_output=True, timeout=5, text=True)
            except subprocess.TimeoutExpired:
                raise ChildProcessError("executable timed out")

            return proc_result.stdout.rstrip()

    @classmethod
    def add_test_case(klass, name, input, expect):
        def test_case(self):
            got = self.execute(input)
            self.assertEqual(expect, got)

        setattr(klass, f"test_{name}", test_case)
