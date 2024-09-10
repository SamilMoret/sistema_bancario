# Sistema Bancário em Python

saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido.")

def saque(valor):
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES_DIARIOS:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"Não é possível sacar valores acima de R$ {limite_saque:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de saque inválido.")

def exibir_extrato():
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato Bancário:")
        for movimento in extrato:
            print(movimento)
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Menu principal
while True:
    print("Bem-vindo ao Banco!")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: R$ "))
        deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: R$ "))
        saque(valor)
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por utilizar o banco. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
