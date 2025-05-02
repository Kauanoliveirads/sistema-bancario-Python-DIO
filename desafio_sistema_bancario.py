menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower().strip()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Opção inválida! Tente novamente.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Opção inválida! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Opção inválida! O valor informado ultrapassa o limite atual.")

        elif excedeu_saque:
            print("Opção inválida! O número de saques feitos ultrapassa o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        
        else:
            print("Opção inválida! Tente novamente.")

    elif opcao == "e":
        print("\n=============== Extrato ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "q":
        print("\nObrigado. Volte sempre!")
        break

    else:
        print("Opção inválida! Tente novamente.")