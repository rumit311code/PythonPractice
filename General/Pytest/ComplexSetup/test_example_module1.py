import pytest

@pytest.mark.usefixtures("setup_module")
class TestExampleOne:

    @pytest.mark.usefixtures("setup_class")
    def test_one(self):
        print("Running TestExampleOne.test_one")
        assert True

    def test_two(self, setup_class):
        print("Running TestExampleOne.test_two")
        assert True

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_example(env):
    print(f"Running tests in {env} environment")
