def calcular_total(valor, cupom):
    if cupom == "AMBOS":
        return "Erro: Não é permitido utilizar mais de um cupom."

    total = valor

    if cupom == "PROMO10":
        if valor >= 100:
            total *= 0.90 
        else:
            return "Erro: O cupom PROMO10 só pode ser usado em compras acima de R$100,00."

    elif cupom == "PRIMEIRACOMPRA":
        total -= 30
        if total < 0:
            total = 0

    if total >= 200:
        frete = 0
    else:
        frete = 25

    total_final = total + frete

    return (
        f"Valor original: R$ {valor:.2f}\n"
        f"Cupom: {cupom}\n"
        f"Frete: R$ {frete:.2f}\n"
        f"Total: R$ {total_final:.2f}"
    )


casos = [
    (200.00, "NENHUM"),
    (199.99, "NENHUM"),
    (99.99, "PROMO10"),
    (100.00, "PROMO10"),
    (50.00, "PRIMEIRACOMPRA"),
    (150.00, "PROMO10"),
    (220.00, "PROMO10"),
    (220.00, "PRIMEIRACOMPRA"),
    (230.00, "NENHUM"),
    (200.00, "AMBOS"),
]

for i, (valor, cupom) in enumerate(casos, start=1):
    print(f"\n===== CT{i:02d} =====")
    print(calcular_total(valor, cupom))
