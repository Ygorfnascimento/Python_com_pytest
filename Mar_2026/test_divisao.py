import pytest

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')
    return a / b


def test_divisao_normal():
    assert dividir(10, 2) == 5


def test_divisao_resultado_float():
    assert dividir(7, 2) == 3.5


def test_divisao_negativos():
    assert dividir(-10, 2) == -5
    assert dividir(10, -2) == -5


def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)