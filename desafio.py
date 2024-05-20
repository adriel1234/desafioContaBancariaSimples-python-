menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = int(input(menu))

    match opcao:
        case 1:
            print("Depósito")
            valor = float(input("Informe um valor para o Depósito: R$ "))
            if valor < 0:
                print("Valor negativo não permitido")
            else:
                saldo = saldo + valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

        case 2:
            print("Saque")
            valor = float(input("Informe um valor para o saque: R$ "))
            excedeu_saldo = valor > saldo
            execedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente. ")
            elif execedeu_limite:
                print("Operação falhou! o valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif saldo > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! o valor informado é inválido.")
        case 3:
            print(f"\n{15*'*'}Extrato{18*'*'}")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print(f"{40*'*'}")
        case 0:
            break
        case _:
            print("Opção invalida")