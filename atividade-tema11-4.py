# Recebe a entrada do usuário
numero_fornecido = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma
soma = 0

# Calcula a soma dos números pares entre 1 e o número fornecido
i = 1
while i <= numero_fornecido:
    if i % 2 == 0:
        soma += i
    i += 1

# Exibe o resultado
print("A soma dos números pares entre 1 e ",numero_fornecido," é: ",soma)