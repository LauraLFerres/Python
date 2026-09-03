#Entrada de dados
total_registros = int(input("Digite a quantidade de registros:"))
quantidade_servidores = int(input("Digite a quantidade de servidores:"))

#Processamento
registros_por_servidor = total_registros / quantidade_servidores

#Saída
print("O servidor deverá processar", registros_por_servidor, "registros")