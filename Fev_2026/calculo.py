def calcule_total(preco,taxa_de_desconto,taxa_de_imposto):
    desconto = preco * taxa_de_desconto
    taxa = (preco - desconto) * taxa_de_imposto
    total = preco - desconto  + taxa
    return round(total,2)