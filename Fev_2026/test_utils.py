def contador(maximo):
    n = 0
    while n < maximo:
        yield n
        n += 1

def test_contador():
    assert list(contador(5)) == [0, 1, 2, 3, 4]