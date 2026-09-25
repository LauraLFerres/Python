from CLASSIFICACAO_OPORTUNIDADE import valor_estimado
from script import dias_sem_contato

d1 = int(input("Último digíto do RM"))
d2 = int(input("Penúltimo digito do RM"))
campanha_ativa = input("Campanha ativa:")
dias_sem_contato = int(input("Dias sem contato:"))
valor_estimado = float(input("Valor estimado:"))

limite_dias = 3 + (d1 % d2)
limite_valor = 500 + 100 * d2

if campanha_ativa == "sim" and dias_sem_contato >= limite_dias:
    print("Urgente")
elif valor_estimado >= limite_valor or dias_sem_contato >= limite_dias:
    print("Priorizar")
else:
    print("Acompanhar")

print(f"{limite_dias}, {limite_valor}")
