# Definir string
string_original = "Exemplo de string para inverter"

# Função para inverter a string manualmente
def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):  # Iterar de trás para frente
        invertida += s[i]
    return invertida

# Chamar a função para inverter a string
string_invertida = inverter_string(string_original)

# String original e invertida
print("Original:", string_original)
print("Invertida:", string_invertida)
