import pytest

def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)

@pytest.fixture(scope="function")
def lista_funcao():
    return [10]

@pytest.fixture(scope="module")
def lista_modulo():
    return [20]

@pytest.fixture(scope="session")
def lista_sessao():
    return [30]

def test_function(lista_funcao):
    assert soma_dobro(lista_funcao) == 20  

def test_module(lista_modulo):
    assert soma_dobro(lista_modulo) == 40  

def test_session(lista_sessao):
    assert soma_dobro(lista_sessao) == 60  