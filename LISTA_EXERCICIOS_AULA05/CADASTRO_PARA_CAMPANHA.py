autorizacao = input("Possui autorização?")
tem_email = input("Possui email?")
tem_whatsapp = input("Tem whatsapp?")

if autorizacao == "sim" and tem_email == "sim" or tem_whatsapp == "sim":
    print("Cadastro pronto")
else:
    print("Cadastro incompleto")