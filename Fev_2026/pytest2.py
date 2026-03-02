def is_positivo(numero):
    return numero > 0

def test_is_positivo():
    assert is_positivo(5) is True
    assert is_positivo(-5) is False
