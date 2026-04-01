import pytest

numeros = [10, 20, 30]
def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)

@pytest.fixture(scope="function")
def fixture_function():
    return 10

@pytest.fixture(scope="module")
def fixture_module():
    return 20

@pytest.fixture(scope="session")
def fixture_session():
    return 30   

def test_1(fixture_function):
    assert soma_dobro([fixture_function]) == 20

def test_2(fixture_module):
    assert soma_dobro([fixture_module]) == 40

def test_3(fixture_session):
    assert soma_dobro([fixture_session]) == 60