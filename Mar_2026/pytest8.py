from pytest7 import*

def test_somar():
    assert somar(2,3) == 5

def test_subtrair():
    assert subtrair(2,3) == 1

def test_multiplicar ():
    assert multiplicar(1,1) == 1

def test_par_ou_par(): 
    assert (par_ou_par % 2 == 0)