from operacoes import (
    soma,
    subtracao,
    multiplicacao,
    divisao,
    resto_divisao,
    media,
    area_retangulo
)

def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(10, 4) == 6

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12

def test_divisao():
    assert divisao(10, 2) == 5

def test_resto_divisao():
    assert resto_divisao(10, 3) == 1

def test_media():
    assert media(6, 6, 6) == 6

def test_area_retangulo():
    assert area_retangulo(5, 4) == 20