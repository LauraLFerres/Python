nivel_interesse = int(input("Nível de interesse: (1 a 3)"))
valor_estimado = float(input("Valor estimado?"))
dias_sem_contato = int(input(""))

if nivel_interesse == "3" and valor_estimado >= 1000:
    print("PRIORIDADE ALTA")
elif nivel_interesse == "3" or dias_sem_contato > 7:
    print("PRIORIDADE MÉDIA")
else
    print("ACOMPANHAMENTO")