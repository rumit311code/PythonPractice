import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_session():
    print("\n[Setup] Session: Initialize resources")
    yield
    print("\n[Teardown] Session: Cleanup resources")

@pytest.fixture(scope="module")
def setup_module():
    print("\n[Setup] Module: Setup per module")
    yield
    print("\n[Teardown] Module: Cleanup per module")

@pytest.fixture(scope="class")
def setup_class():
    print("\n[Setup] Class: Setup per test class")
    yield
    print("\n[Teardown] Class: Cleanup per test class")

def pytest_addoption(parser):
    ### action: store ###
    # Stores value as a string.
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against")

    ### action: store_const ###
    # Stores a predefined "const" value if the option is specified.
    # Stores a predefined "default" value if the option is unspecified.
    parser.addoption(
        "--mode",
        action="store_const",
        const="debug",
        default="release",
        help="Set debug mode")
    """
    def test_mode(request):
        mode = request.config.getoption("--mode")
        assert mode == "release"  # Default
    
    $ pytest -v  # mode="release"
        PASSED

    $ pytest -v --mode  # mode="debug"
        PASSED  # If test expects "debug"
    """

    ### action: store_true ###
    # Sets the option’s value to True if the option is specified.
    # useful for boolean flags.
    parser.addoption(
        "--runslow",
        action="store_true",
        help="Run slow test.")
    """
    @pytest.fixture
    def runslow(request):
        return request.config.getoption("--runslow")
    
    @pytest.mark.slow
    def test_slow(runslow):
        if not runslow:
            pytest.skip("need --runslow to run")
        assert True
    
    $ pytest -v test_module.py  # Skips slow test
        test_module.py::test_slow SKIPPED

    $ pytest -v test_module.py --runslow
        PASSED
    """

    ### action: store_false ###
    # Sets the option’s value to False if the option is specified.
    parser.addoption(
        "--no-coverage",
        action="store_false",
        help="Disable coverage reporting")
    """
    @pytest.fixture
    def coverage(request):
        return request.config.getoption("--no-coverage")
        
    def test_with_coverage(coverage):
        assert coverage is True  # Passes without --no-coverage
    
    $ pytest -v
        test_example.py::test_with_coverage PASSED

    $ pytest -v --no-coverage
        test_example.py::test_with_coverage FAILED  # coverage is False
    """

    ### action: append ###
    # When called like pytest --tag=fast --tag=slow, the resulting list will be ['fast', 'slow'].
    parser.addoption(
        "--tags",
        action="append",
        default=[],
        help="test tags to include")
    """
    @pytest.fixture
    def tags(request):
        return request.config.getoption("--tags")
    
    def test_with_tags(tags):
        assert "fast" in tags  # Fails without --tags
    
    $ pytest -v  # tags=[]
        FAILED

    $ pytest -v --tags fast --tags slow
        PASSED  # tags=["fast", "slow"]
    """

    ### action: append_const ###
    # Appends a "const" value to a list each time the option is specified.
    parser.addoption(
        "--extra",
        action="append_const",
        const="feature_x",
        default=[],
        help="Add extra feature")
    """
    @pytest.fixture
    def extras(request):
        return request.config.getoption("--extra")
        
    def test_extras(extras):
        assert len(extras) == 0  # No --extra

    $ pytest -v
        PASSED

    $ pytest -v --extra --extra
        FAILED  # extras=["feature_x", "feature_x"]
    """

    ### action: count ###
    # Returns the count of occurrences of the option on the command line.
    # If not specified, returns the "default" value.
    parser.addoption(
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity level")
    """
    @pytest.fixture
    def verbosity(request):
        return request.config.getoption("--verbose")

    def test_verbosity(verbosity):
        assert verbosity == 0  # No flags

    $ pytest -v
        PASSED

    $ pytest -v --verbose --verbose
        FAILED  # verbosity=2
    """