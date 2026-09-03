#Entrada de dados
usuarios_iniciais = int(input("Digite o número inicial de usuários:"))
meses = int(input("Digite a quantidade de meses:"))

#Processamento
usuarios_finais = usuarios_iniciais * meses

#Saída
print("Total de usuários após", meses, "meses:", usuarios_finais)