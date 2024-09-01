def analise_faturamento(dados):
    """
    Analisa os dados de faturamento, ignorando dias sem faturamento.
    Retorna o menor valor, maior valor e o número de dias acima da média.
    """
    # Ignora dias sem faturamento
    valores = [valor for valor in dados if valor > 0]

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

# Bloco opcional para execução direta
if __name__ == "__main__":
    dados = [
        5000, 3000, 0, 4000, 3500, 0, 0, 7000, 6000, 2000, 0, 4500
    ]
    menor, maior, dias_acima_media = analise_faturamento(dados)
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Número de dias acima da média: {dias_acima_media}")
