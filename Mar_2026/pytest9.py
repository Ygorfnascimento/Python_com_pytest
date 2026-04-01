import pytest

@pytest.fixture(scope="function")
def fixture_function():
    return 10

@pytest.fixture(scope="function")
def fixture_function():
    return 20

@pytest.fixture(scope="function")
def fixture_module():
    return 30

def test_1(fixture_function):
    assert fixture_function == 20

def test_2(fixture_function, fixture_module):
    assert fixture_function == 20
    assert fixture_module == 30