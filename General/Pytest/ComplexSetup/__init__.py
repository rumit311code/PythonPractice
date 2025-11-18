"""
Commonly used runtime parameters/flags for the pytest command include:

    -v or --verbose: Increase verbosity of test output to show individual test results.

    -q or --quiet: Reduce output verbosity.

    -k <expression>: Run tests that match the given substring expression or test name pattern.

    -m <markexpr>: Run tests with specific pytest markers (e.g., -m smoke).

    --maxfail=N: Stop after N failures.

    --tb=short|long|line|no: Control traceback format for failures.

    -s: Disable output capturing, allowing print statements to be seen live.

    --lf or --last-failed: Run only the tests that failed on the last run.

    --ff or --fail-first: Run the last failures first.

    --maxfail=N: Stop after N failures.

    --disable-warnings: Suppress warning output.

    --tb=short: Show shorter tracebacks for easier reading.

    --junitxml=path: Create a JUnit XML report at the specified path.

    --capture=no: Disable output capture completely.

    --setup-show: Show setup and teardown of fixtures in the output.

    --durations=N: Show slowest N tests for performance analysis.

"""