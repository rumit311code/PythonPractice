import pytest

# Basic function fixture
@pytest.fixture
def input_value():
    return 10

def test_check_difference(input_value):
    assert input_value - 2 == 8

# Parameterized fixture
@pytest.fixture(params=[1, 2, 3])
def param_val(request):
    return request.param

def test_param_example(param_val):
    print(f"testing param_val: {param_val}")
    assert param_val in [1, 2, 3]

# Fixture with scope
# @pytest.fixture(scope="module")
# def db_connection():
#     conn = create_db_connection()
#     yield conn
#     conn.close()
#
# def test_db1(db_connection):
#     assert db_connection.is_connected()

# Dependent fixtures
@pytest.fixture
def user():
    return {"name": "Alice"}

@pytest.fixture
def user_profile(user):
    user["profile"] = "admin"
    return user

def test_user_profile(user_profile):
    print(f"testing user_profile: {user_profile}")
    assert user_profile["profile"] == "admin"

# Auto use fixtures
@pytest.fixture(autouse=True)
def auto_setup():
    print("This always runs before each test.")

def test_something():
    assert True

# Yield Fixtures, useful for teardown
@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "temp.txt"
    with open(file, "w") as f:
        f.write("hello")
    yield file
    file.unlink()  # Teardown after test


