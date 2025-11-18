import pytest

@pytest.mark.usefixtures("setup_module")
class TestExampleTwo:

    @pytest.mark.usefixtures("setup_class")
    def test_three(self):
        print("Running TestExampleTwo.test_three")
        assert True

    def test_four(self, setup_class):
        print("Running TestExampleTwo.test_four")
        assert True
