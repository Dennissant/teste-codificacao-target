from percentual_representacao import calcular_percentuais

def test_calcular_percentuais():
    dados = {
        'SP': 3753,
        'RJ': 2029,
        'MG': 1617,
        'ES': 1503,
        'Outros': 1098
    }
    percentuais = calcular_percentuais(dados)
    assert round(percentuais['SP'], 2) == 37.53
    assert round(percentuais['RJ'], 2) == 20.29
    assert round(percentuais['MG'], 2) == 16.17
    assert round(percentuais['ES'], 2) == 15.03
    assert round(percentuais['Outros'], 2) == 10.98
