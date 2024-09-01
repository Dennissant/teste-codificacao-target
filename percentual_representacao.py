def calcular_percentuais(dados):
    """
    Calcula os percentuais de cada estado com base nos dados fornecidos.
    """
    total = sum(dados.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in dados.items()}
    return percentuais

if __name__ == "__main__":
    dados = {
        'SP': 3753,
        'RJ': 2029,
        'MG': 1617,
        'ES': 1503,
        'Outros': 1098
    }
    percentuais = calcular_percentuais(dados)
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")
