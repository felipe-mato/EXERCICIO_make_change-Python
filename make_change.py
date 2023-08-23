def make_change(moedas, troco):
    moedas_organizadas = sorted(moedas, reverse=True)
    response = []
    valor = troco
    for i in moedas_organizadas:
        qtd_moedas = valor // i
        valor_restante = valor % i
        valor = valor_restante
        response.append((f'{qtd_moedas} moedas', f'{i} centavos'))
    print(response)

moedas = [5, 25, 1, 10]
make_change(moedas, 73)