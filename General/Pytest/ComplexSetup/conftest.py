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
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
    parser.addoption("--verbose-level", action="count", default=0, help="Increase verbosity level")
    parser.addoption("--debug", action="store_true", help="Enable debug mode")
    parser.addoption("--no-cleanup", action="store_false", help="Skip cleanup after tests")
    parser.addoption("--mode", action="store", default="default", help="Select mode")

    parser.addoption(
            "--enable-feature",
            action="append_const",
            const="feature_x",
            help="Enable feature_x"
        )

    parser.addoption(
            "--tag",
            action="append",
            help="Add tags to filter tests"
        )
    # When called like pytest --tag=fast --tag=ui, the resulting list will be ['fast', 'ui'].

    parser.addoption(
        "--verbosity",
        action="store_const",
        const=2,
        default=1,
        help="Set verbosity level to 2"
    )

    """
    The action parameter in parser.addoption in pytest determines the way command line options handle the input values. 
    Common values for the action parameter are:

    store (default): Stores the option’s argument as a string.
    store_true: Sets the option’s value to True if the option is specified; useful for boolean flags.
    store_false: Sets the option’s value to False if the option is specified.
    store_const: Stores a constant value when the option is specified.
    append: Appends each argument to a list; useful for options that can be specified multiple times.
    append_const: Appends a constant value to a list each time the option is specified.
    count: Counts the number of times the option appears on the command line; useful for verbosity flags.
    """