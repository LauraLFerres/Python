#Entrada
largura_quarto = int(input("Digite a largura do quarto escolhido:"))
comprimento_quarto = int(input("Digite o comprimento do quarto escolhido:"))
n_pessoas_aparelhos = int(input("Digite a quantidade de pessoas ou aparelhos:"))

#Processamento
BTUS = 600 * largura_quarto * comprimento_quarto + 600 * n_pessoas_aparelhos

#Saída
print("O número mínimo de BTUS é: ", BTUS)