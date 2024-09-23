import json

def analise_faturamento(faturamento):
    # Filtrando apenas dias com faturamento maior que zero
    faturamento = [f["valor"] for f in faturamento if f["valor"] > 0]

    # Calculando o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)

    # Calculando a média mensal
    media_mensal = sum(faturamento) / len(faturamento)

    # Calculando o número de dias com faturamento superior à média
    dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados["faturamento"]

# Verificando
caminho_arquivo = 'faturamento.json'  # Caminho para o arquivo JSON
faturamento_diario = carregar_dados_json(caminho_arquivo)
menor, maior, dias_acima_media = analise_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
