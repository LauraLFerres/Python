bateria_robo = float(input("Bateria do robô restante: "))
temperatura_motor = float(input("Temperatura do motor: "))
rota_bloqueada = input("A rota está bloqueada? ")

if bateria_robo < 25:
    print("Missão cancelada: bateria insuficiente")
else:
    if temperatura_motor > 80:
        print("Missão cancelada: superaquecimento")
    else:
        if rota_bloqueada == "sim":
            print("Missão autorizada com atenção: rota bloqueada")
        else:
            print("Missão autorizada.")