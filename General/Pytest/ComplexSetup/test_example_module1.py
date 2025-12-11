import pytest

# fixture applies to all methods in a test class.
@pytest.mark.usefixtures("setup_module")
class TestExampleOne:

    # use this syntax if fixture does not return any value
    @pytest.mark.usefixtures("setup_class")
    def test_one(self):
        print("Running TestExampleOne.test_one")
        assert True

    # use this syntax if fixture returns a value that is needed.
    def test_two(self, setup_class):
        print("Running TestExampleOne.test_two")
        assert True

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_example(env):
    print(f"Running tests in {env} environment")
