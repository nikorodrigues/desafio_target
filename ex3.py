#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
#  faça um programa, na linguagem que desejar, que calcule e retorne:
#   • O menor valor de faturamento ocorrido em um dia do mês;
#   • O maior valor de faturamento ocorrido em um dia do mês;
#   • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#FUNÇÃO ANÁLISE DO FATURAMENTO
def analise_faturamento(faturamento):
    # Removendo dias sem faturamento (dias com faturamento zero)
    # f for f in faturamento: percorre todos os elementos f da lista de faturamento.
    # if f > 0: mantém apenas os valores maiores que zero.
    faturamento = [f for f in faturamento if f > 0]

    # Calculando o menor e o maior valor de faturamento
    # min(faturamento) retorna o menor valor na lista de faturamento.
    menor_faturamento = min(faturamento)
    # max(faturamento) retorna o maior valor na lista de faturamento.
    maior_faturamento = max(faturamento)

    # Calculando a média mensal
    # sum(faturamento) soma todos os valores da lista de faturamento (excluindo zeros).
    # len(faturamento) retorna o número de dias que tiveram faturamento (não contando os dias com faturamento zero)
    # sum(faturamento) / len(faturamento) obtém a média de faturamento diário no período
    media_mensal = sum(faturamento) / len(faturamento)

    # Calculando o número de dias com faturamento superior à média
    # 1 for f in faturamento if f > media_mensal: para cada valor f na lista de faturamento, 
    # se f for maior que a média, adicionamos 1 à contagem. 
    dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Verificando (15)
faturamento_diario = [200, 300, 0, 150, 600, 0, 400, 800, 0, 700, 1000, 550, 0, 400, 700] 
# Vetor de faturamento diário
menor, maior, dias_acima_media = analise_faturamento(faturamento_diario)

print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
