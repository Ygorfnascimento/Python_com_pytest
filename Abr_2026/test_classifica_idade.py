import pytest 
from classifica_idade import classifica_idade

@pytest.mark.crianca
@pytest.mark.parametrize("idade", [0, 5, 11])
def test_crianca(idade):
    assert classifica_idade(idade) == "Criança"

@pytest.mark.adolescente
@pytest.mark.parametrize("idade", [12, 15, 17])
def test_adolescente(idade):
    assert classifica_idade(idade) == "Adolescente"

@pytest.mark.adulto
@pytest.mark.parametrize("idade", [18, 30, 59])
def test_adulto(idade):
    assert classifica_idade(idade) == "Adulto"

@pytest.mark.idoso
@pytest.mark.parametrize("idade", [60, 75, 100])
def test_idoso(idade):
    assert classifica_idade(idade) == "Idoso"