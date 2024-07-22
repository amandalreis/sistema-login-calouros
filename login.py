import os

usuario_logado = False

def mostrar_menu():
    os.system('clear') #Para limpar o terminal, apenas por fins estéticos.
    print("Bem-vindo ao Sistema de Login!")
    print("1. Fazer login")
    print("2. Somar valores")
    print("3. Multiplicar valores")
    print("4. Número par ou ímpar?")
    print("5. Sair do sistema")
    opcao = int(input("Selecione uma das opções acima: ")) #Para solicitar e receber um valor do usuário através do terminal

    if opcao == 1:
        fazer_login()
    elif opcao == 2:
        somar_valores(usuario_logado)
    elif opcao == 3:
        multiplicar_valores(usuario_logado)
    elif opcao == 4:
        numero_par_ou_impar(usuario_logado)
    elif opcao == 5:
        sair()
    else:
        os.system('clear')
        print("Valor inválido.")
        voltar_ao_menu()

def voltar_ao_menu():
    input("Insira qualquer valor para voltar ao menu:")
    mostrar_menu()

def fazer_login():
    global usuario_logado
    os.system('clear')
    usuarios = {
        "amandalreis": "senha1",
        "reynanvt": "senha2",
        "rod_arth": "senha3"
    }

    username = input("Insira o seu username: ")
    senha = input("Insira a sua senha: ")

    if username in usuarios:
        if usuarios[username] == senha:
            usuario_logado = True
            print("Login realizado com sucesso!")
            voltar_ao_menu()
        else:
            print("ERRO: Senha incorreta!")
            voltar_ao_menu()
    else:
        print("ERRO: Não existe um usuário com esse username!")
        voltar_ao_menu()

def somar_valores(usuario_logado):
    if usuario_logado:
        print("Quais números você deseja somar?")
        numero_1 = float(input("Número 1: "))
        numero_2 = float(input("Número 2: "))
        print(f"O resultado é {numero_1 + numero_2}")
        voltar_ao_menu()
    else:
        print("É necessário realizar login para somar valores!")
        voltar_ao_menu()

def multiplicar_valores(usuario_logado):
    if usuario_logado:
        print("Quais números você deseja multiplicar?")
        numero_1 = float(input("Número 1: "))
        numero_2 = float(input("Número 2: "))
        print(f"O resultado é {numero_1 * numero_2}")
        voltar_ao_menu()
    else:
        print("É necessário realizar login para multiplicar valores!")
        voltar_ao_menu()

def numero_par_ou_impar(usuario_logado):
    if usuario_logado:
        print("Qual número inteiro você deseja saber se é par ou ímpar?")
        numero = float(input("Digite o número: "))
        if numero % 2 == 0:
            print(f"O número {numero} é par")
        else:
            print(f"O número {numero} é ímpar")
        voltar_ao_menu()
    else:
        print("É necessário realizar login para verificar se um número é par ou ímpar!")
        voltar_ao_menu()

def sair():
    os.system('clear')
    print("Até mais! Encerrando execução... :)")
    exit()

mostrar_menu()
