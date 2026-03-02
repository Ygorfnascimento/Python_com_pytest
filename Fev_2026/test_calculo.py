import pytest
from calculo import calcule_total

@pytest.mark.parametrize(
    "preco, taxa_de_desconto, taxa_de_imposto",
    [
        (100, 0.10, 0.05),
        (200, 0.20, 0.10),
        (50, 0.05, 0.02),
    ]
)
def test_calculo_total(preco, taxa_de_desconto, taxa_de_imposto):
    expected_discount = preco * taxa_de_desconto
    preco_com_desconto = preco - expected_discount
    expected_tax = preco_com_desconto * taxa_de_imposto
    expected_total = preco_com_desconto + expected_tax

    assert calcule_total(preco, taxa_de_desconto, taxa_de_imposto) == expected_total