# entrada de dados e conversão de tipos
nivelInteresse = int(input("Digite o nível de interesse (1 a 3): "))
tempoSemContato = int(input("Digite os dias sem contato: "))
valorDeApoio = float(input("Digite o valor estimado de apoio: "))
situacaoCampanha = input("A campanha está ativa? (Sim/Não): ")

# regras de classificação de prioridade:
# requisito 'RETORNO IMEDIATO': maior nível de interesse (3) e campanha ativa ("sim") simultaneamente.
if nivelInteresse == 3 and situacaoCampanha.lower() == "sim":
    prioridade = "RETORNO IMEDIATO"
    acao = "realizar contato hoje"
elif nivelInteresse == 3 or valorDeApoio >= 5000:
    prioridade = "PRIORIDADE ALTA"
    acao = "preparar retorno em até 24 h"
elif nivelInteresse == 2 or tempoSemContato > 5:  # mais de 5 dias sem contato
    prioridade = "PRIORIDADE MÉDIA"
    acao = "agendar acompanhamento"
else:
    prioridade = "ACOMPANHAMENTO"
    acao = "manter no fluxo normal de relacionamento"

# saída formatada exatamente conforme a especificação do projeto
print(f"\nNível de interesse informado: {nivelInteresse}")
print(f"Dias sem contato: {tempoSemContato}")
print(f"Valor estimado de apoio: R$ {valorDeApoio:.2f}")
print(f"Campanha ativa: {situacaoCampanha}")
print()
print(f"Prioridade calculada: {prioridade}")
print(f"Ação sugerida: {acao}")