import pytest
import time


def soma(a, b):
    return a + b


def multiplicacao(a, b):
    return a * b


@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert soma(2, 2) == 4


@pytest.mark.rapido
def test_soma_rapida():
    assert soma(2, 3) == 5

@pytest.mark.lento
def test_multiplicacao_lenta():
    time.sleep(2)
    assert multiplicacao(3, 3) == 9


@pytest.mark.rapido
def test_multiplicacao_rapida():
    assert multiplicacao(3, 3) == 9