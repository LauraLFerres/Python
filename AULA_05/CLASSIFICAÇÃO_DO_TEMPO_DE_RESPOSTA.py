tempo_resposta = int(input("Digite a velocidade da API:"))

if tempo_resposta == 100:
    classificacao = "Excelente"
elif tempo_resposta <= 300:
    classificacao = "Aceitável"
elif tempo_resposta <= 800:
    classificacao = "Lento"
else:
    classificacao = "Crítico"

print("Desempenho do serviço:", classificacao)