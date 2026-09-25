dias_sem_contato = input("A quantos dias não há contato?")
nivel_interesse = input("Qual o nível de interesse? (1,2 ou 3)")

if dias_sem_contato >= "7" or nivel_interesse == "3":
    print("Realizar retorno.")
else:
    print("Manter acompanhamento.")

print(f"{dias_sem_contato, nivel_interesse}")