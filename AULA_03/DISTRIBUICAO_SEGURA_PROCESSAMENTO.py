# Entrada de dados
registros = int(input("Total de registros:"))
servidores = int(input("Quantidade de servidores:"))

# Evita divisão por zero
if servidores == 0:
    print("divisão impossível")
else:
    por_servidor = registros / servidores
    print(por_servidor, "registro por servidor")