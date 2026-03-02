from pytest4 import*

def test_email_validate():
    assert email_valido("exemplo@eemail.com") is True
    assert email_valido("exemplo.com") is False

def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None