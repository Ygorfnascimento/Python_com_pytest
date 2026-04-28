import pytest

def fatorial(n):
    if n < 0:
        raise ValueError("Número negativo")
    if n == 0:
        return 1
    return n * fatorial(n-1)

@pytest.mark.parametrize("n, esperado", [
    (0, 1),
    (1, 1),
    (5, 120)
])
def test_fatorial(n, esperado):
    assert fatorial(n) == esperado

def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-1)