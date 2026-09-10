bateria_drone = float(input("Bateria do drone(%):"))
velocidade_vento = float(input("Velocidade do vento(km):"))
peso_carga = float(input("Peso do carga(kg):"))

if bateria_drone < 30:
    print("Missão cancelada: bateria fraca.")
else:
    if velocidade_vento > 40:
        print("Missão cancelada: vento forte")
    else:
        if peso_carga > 5:
            print("Missão autorizada com alerta: carga pesada.")
        else:
            print("Missão autorizada.")