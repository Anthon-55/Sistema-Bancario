menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

def estratoCalculo():
    est = ""
    for i in extrato:
        est += f'{i} \n'
    est += f'Saldo: R$ {saldo:.2f}'
    return est

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso.")
            extrato.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                numero_saques += 1
                print("Saque realizado com sucesso.")
                extrato.append(f"Saque: R$ {valor:.2f}")
            else:
                print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("========== EXTRATO ==========")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(estratoCalculo())
        # print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


