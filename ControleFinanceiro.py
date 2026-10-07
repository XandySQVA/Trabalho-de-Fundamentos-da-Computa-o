opcao = int(0)
gastoAlimento = float(0)
gastoTransporte = float(0)
rendaMensal = float(0)
gastoTotal = float(0)
gastoOnline = float(0)
gastoContas = float(0)


while opcao != 6:
    print("------------------------------------ \n \t CONTROLE FINANCEIRO \n------------------------------------")
    print("1 - Informar renda mensal \n2 - Cadastrar gasto \n3 - Consultar gastos \n4 - Consultar situação financeira \n5 - Ver estatísticas \n6 - Sair")
    print("-----------------------------------")
    diferenca = rendaMensal - gastoTotal
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        rendaMensal = float(input("Digite sua renda mensal: "))
        print("Renda Mensal cadastrada")
    elif opcao == 2:
        print("---------------------------- \n1 - Alimento \n2 - Transporte \n3 - Contas \n4 - Produtos Online")
        tipodeGasto = int(input("Escolha uma opção de gasto: "))
        match tipodeGasto:
            case 1:
                gastoAlimento = float(input("Digite o Gasto com alimento: "))
            case 2:
                gastoTransporte = float(input("Digite o gasto com o transporte: "))
            case 3:
                gastoContas = float(input("Digite o gasto com as contas: "))
            case 4:
                gastoOnline = float(input("Digite o gasto com compras online: "))
        gastoTotal = gastoOnline + gastoContas + gastoAlimento + gastoTransporte

    elif opcao == 3:
        print(f"Seus gastos totais foram R${gastoTotal}")
    elif opcao == 4:

        print(f"Seu saldo atual é: R${diferenca}")
    elif opcao == 5:
        print(f"------------------------Você teve a renda de R$ {rendaMensal}------------------------")
        print(f"Seus gastos com alimentos foram R${gastoAlimento}\nSeus gastos com transporte foram R${gastoTransporte}\nSeus gastos com contas foram R${gastoContas}\nSeus gastos com produtos online foram R${gastoOnline}")
        print(f"Seu saldo restante é de R${diferenca}")
    elif opcao == 6:
        print("Sair")
    else:
        print("Inválida")
