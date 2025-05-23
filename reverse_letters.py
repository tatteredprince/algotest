#!/usr/bin/env python
"""
Test external executable for reverse letters.

By default the executable gets a text to reverse letters in words.
"""
import unittest
import algotest


class TestReverseLetters(algotest.AlgoTest):
    pass


if __name__ == "__main__":
    for case in [
        ["one_to_three", "one two three", "eno owt eerht"],
        ["hello_world", "Hello, world!", "olleH, dlrow!"],
        ["whitespace_left_right", " abc ", " cba "],
        ["whitespace_left", " abc", " cba"],
        ["whitespace_right", "abc ", "cba "],
        ["hyphen", "semi-authomatic", "imes-citamohtua"],
        ["palindrome", "tenet", "tenet"],
        ["sentence", "Able was I ere I saw Elba", "elbA saw I ere I was ablE"]
    ]:
        TestReverseLetters.add_test_case(*case)

    unittest.main()
