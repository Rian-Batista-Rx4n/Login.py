def hud(msg="TELA DE LOGIN"):
    from time import sleep as s
    print("="*50)
    print()
    print(f"{msg:^50}")
    try:
        ola = f"Olá {usuario}!"
        print(f"{ola:^50}")
        print()
    except:
        print()
    print("="*50)
    s(1)


def criararquivo(nome):
    from time import sleep as s
    try:
        a = open(nome, "rt")
        a.close()
    except:
        hud()
        print("Arquivo não existe!")
        s(1)
        print("Criando Arquivo...")
        s(2)
        print("\n"*100)
        a = open(nome, "wt+")
        a.close()


def leraquivo(nome):
    from time import sleep as s
    print("\n" * 100)
    hud()
    try:
        arquivo = open(nome, "rt")
    except:
        print("Não foi possivel ler o arquivo!")
    else:
        print("Nossos Membros:\n")
        for item in arquivo:
            info = item.split(";")
            info[1] = info[1].replace("\n", "")
            print(info[0])
        s(1)
        input("\nAperte ENTER para continuar...")
        print("\n" * 100)
        arquivo.close()


def registrar(nome):
    print("\n" * 100)
    hud()
    try:
        arquivo = open(nome, "rt")
    except:
        print("Arquivo não existe!")
    else:
        from time import sleep as s
        while True:
            login = str(input("Login: ")).strip()
            existe = 0
            for item in arquivo:
                info = item.split(";")
                info[1] = info[1].replace("\n", "")
                verificar = str(info[0])
                if verificar == login:
                    print("Usúario já existente!")
                    s(1)
                    existe = 1
            if existe != 1:
                arquivo.close()
                arquivo = open(nome, "at")
                senha = str(input("Senha: ")).strip()
                arquivo.write(f"{login};{senha}\n")
                arquivo.close()
                s(1)
                print("\nRegistro realizado com Sucesso!")
                s(2)
                input("\nAperte ENTER para continuar...")
                print("\n"*100)
                break


def logar(nome):
    from time import sleep as s
    global usuario
    print("\n" * 100)
    hud()
    try:
        arquivo = open(nome, "rt")
        arquivo.close()
    except:
        print("Erro ao ler arquivo!")
    else:
        tente = 0
        while True:
            arquivo = open(nome, "rt")
            if tente == 3:
                s(1)
                print("\nJá acabaram as tentivas\nTente realizar um registro...")
                s(5)
                print("\n"*100)
                break
            login = str(input("Login: ")).strip()
            senha = str(input("Senha: ")).strip()
            permi = 0
            for item in arquivo:
                info = item.split(";")
                info[1] = info[1].replace("\n", "")
                verificar1 = str(info[0])
                verificar2 = str(info[1])
                if verificar1 == login and verificar2 == senha:
                    permi += 1
            if permi == 1:
                arquivo.close()
                usuario = login
                print("\nLogin efetuado com SUCESSO!")
                s(2)
                input("Aperte ENTER para continuar...")
                print("\n"*100)
                break
            else:
                print("Login ou Senha INCORRETA!")
                arquivo.close()
                tente += 1


arq = "usuarios.csv"
criararquivo(arq)

while True:
    hud()
    print("""[1] Fazer Login
[2] Realizar Registro
[3] Ver Usúarios

[9] Sair""")
    try:
        opc = int(input(">> "))
    except:
        print("Valor Invalido!")
    else:
        opc = opc
        if opc != 1 and opc != 2 and opc != 3 and opc != 9:
            print("Valor Indisponivel!")

        if opc == 1:
            logar(arq)

        elif opc == 2:
            registrar(arq)

        elif opc == 3:
            leraquivo(arq)

        elif opc == 9:
            print("Obrigado por utilizar meu programa!\nBy: RX4N")
            break
