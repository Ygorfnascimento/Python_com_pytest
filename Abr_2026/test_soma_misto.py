def soma (a,b):
    return a + b

def test_soma_positivo():
    assert soma (2,3) == 5

def test_soma_negativo():
    assert soma (-1,-1) == -2

def test_soma_misto():
    assert soma (-1,1) == 0