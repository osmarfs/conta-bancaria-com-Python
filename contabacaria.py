import os
def banco():
    n = 0
    sac = 0
    dp = 0
    saldo = []
    saldoataul = sum(saldo)
    conta = ["conta corrente", "conta poupança"]
    ligado =  True
    contacriada = False
    
    try:
        while ligado:            
            print("[1] criar uma conta\n"
                    "[2] depositar\n"
                    "[3] sacar\n"
                    "[4] consultar saldo\n"
                    "[5] fechar conta\n"
                    "[6] encerrar atendimento")

            escolha = int(input("Digte a opção desejada: "))
            if escolha == 1:
                print("para começarmos gostaria de saber se está com os documentos em mãos?\n"
                        "se sim aperte [1], se não aperte [2]")
                doc = int(input())
                if doc == 1:
                    nome = str(input("digite seu nome: "))
                    cpf = int(input("Digite seu CPF: "))
                    tipo_conta = int(input("Qual o tipo de conta [1]corrente ou [2]poupança: "))
                    if tipo_conta == 1:
                        tipo_conta = conta[1]
                        contacriada = True
                    elif tipo_conta == 2:
                        tipo_conta = conta[0]
                        contacriada = True
                    print(f"conta de {nome} cpf num {cpf} do tipo {tipo_conta}\n"
                            f"criada com sucesso!")
                    
                else:
                    print("Volte quand estiver com os documentos!")
                    break
            elif escolha == 2:
                if contacriada:
                    dp = int(input("Digite o valor a ser depositado: "))
                    saldo.append(dp)
                    print(f"seu saldo atua é {sum(saldo)}")
                    esco = int(input("Deseja continuar o atendimento ou encerrar\n"
                                        "[1] para continuar o atendimento"
                                        "[2] para encerrar"))
                    if esco == 1:
                        continue
                    else:
                        break
                else:
                    print("Você precisa criar uma conta primeiro.")
            elif escolha == 3:
                if contacriada:
                    sac = int(input("Quanto deseja sacar: "))
                    if sum(saldo) <= 0:
                        print(f"não há valores para serem sacados, pois seu saldo é R${sum(saldo):.2f}")
                    elif sum(saldo) > 0 and sum(saldo) < sac:
                        print(f"O valor que está solicitando é maior do que o do saldo, saldo atual R${sum(saldo):.2f}")
                    elif sum(saldo) >= sac:
                        saldo.append(- sac)
                        print(f"R${sac:.2f} sacado com sucesso, saldo da conta R${sum(saldo):.2f}")
                else:
                    print("Você precisa criar uma conta primeiro.")
            elif escolha == 4:
                if contacriada:
                    print(f"Extrato da conta\n"
                            f"Nome: {nome}\n"
                            f"CPF: {cpf}\n"
                            f"Saldo: {sum(saldo):.2f}")
                else:
                    print("Você precisa criar uma conta primeiro.")
            elif escolha == 5:
                if contacriada:
                    if sum(saldo) > 0:
                        print(f"Você não pode fechar a conta se não sacar seu saldo\n"
                                f"saldo no valor de {sum(saldo)}")
                    else:
                        print(f"Conta fechada com sucesso!")
                        break
                else:
                    print("Você precisa criar uma conta primeiro.")
            elif escolha == 6:
                ligado = False
            else:
                print("opção errada, escolha umas das opções na tela!")
    except:
        print("uttilize apenas os caracteres válidos!")
banco()