from analise_faturamento import analise_faturamento

def test_analise_faturamento():
    dados = [
        5000, 3000, 0, 4000, 3500, 0, 0, 7000, 6000, 2000, 0, 4500
    ]
    menor, maior, dias_acima_media = analise_faturamento(dados)
    assert menor == 2000
    assert maior == 7000
    assert dias_acima_media == 4
