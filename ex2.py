#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne
# uma mensagem avisando se o número informado pertence ou não a sequência.


def verifica_fibonacci(num):
    # Dois primeiros valores da sequência Fibonacci
    a = 0
    b = 1
    # Enquanto 'a' for menor ou igual ao número, continuamos gerando a sequência
    while a <= num:
        # Se encontrarmos o número, retornamos que ele pertence à sequência
        if a == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        # Atualizamos os valores de 'a' e 'b' para os próximos números da sequência
        a = b
        b = a + b
    # Se sair do loop, significa que o número não pertence à sequência
    return f"O número {num} não pertence à sequência de Fibonacci."

# Alterar o valor da variável num para descobrir se o número pertence a sequência de Fibonnaci
num = 2
resultado = verifica_fibonacci(num)
print(resultado)
