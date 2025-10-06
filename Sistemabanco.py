# ==========================================
# SISTEMA BANCÁRIO EM PYTHON
# Funções: Depósito, Saque e Extrato
# ==========================================

# Variáveis principais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop principal do sistema
while True:
    print("\n======= MENU =======")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[4] Sair")
    print("====================")

    opcao = input("Escolha uma opção: ")

    # --- DEPÓSITO ---
    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")

    # --- SAQUE ---
    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Operação falhou! O limite por saque é R$ {limite:.2f}.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido.")

    # --- EXTRATO ---
    elif opcao == "3":
        print("\n======= EXTRATO =======")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("========================")

    # --- SAIR ---
    elif opcao == "4":
        print("\nObrigado por usar o sistema bancário! Até logo.")
        break

    # --- OPÇÃO INVÁLIDA ---
    else:
        print("\nOpção inválida! Tente novamente.")