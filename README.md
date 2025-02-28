Validate computational algorithms, run tests against external binary.

Set path to external binary as first command line argument in tests run: 
```bash
$ algotest/array_sorting.py /path/to/the/external/executable
...............
----------------------------------------------------------------------
Ran 15 tests in 0.034s

OK
```

By default the executable gets test cases from standard input.
 
If the executable proccesses test cases from command line arguments set second command line argument as logically true value:
```bash
$ algotest/array_sorting.py /path/to/the/external/executable 1
...............
----------------------------------------------------------------------
Ran 15 tests in 0.034s

OK
```

Tests use Python's standard `unittest`, no additional dependencies are required.

This repository provides tests for algorithms:
- Array sorting
- Binary search
- Digit sum
- Factorial
- Fibonacci sequence
- Monotonic sequence
- Reverse letters
- Zip arrays