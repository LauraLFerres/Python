erros_encontrados = float(input("Digite a quantidade de erros encontrados: "))

if erros_encontrados == 0:
    print("Sistema estável")
elif erros_encontrados >= 5:
    print("Sístema crítico")
elif erros_encontrados >= 0:
    print("Ajustes necessário")
else:
    print("Entrada inválida")