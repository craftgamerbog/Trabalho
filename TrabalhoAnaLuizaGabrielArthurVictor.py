print("seja bem vindo ao seu gerenciador de estoques")
senha = input("primeiramente, crie uma senha!  ""ela será usada para interromper o programa, se necessário ")
item1 = "NADA"
item2 = "NADA"
item3 = "NADA"
item4 = "NADA"
item5 = "NADA"
fecho = senha
while True:
    print("deseja VER, ADICIONAR, REMOVER ou MUDAR QUANTIDADE")
    oqfazer = input("Desejo: ")
    if oqfazer == "ADICIONAR" or oqfazer == "adicionar" or oqfazer == "Adicionar":
        if item1 == "NADA":
            item1 = input("digite somente o item que deseja adicionar: ")
            quantidade1 = int(input("agora digite a quantidade que deseja adicionar: "))
            print("ok",quantidade1,item1,"foi adicionado!")
        elif item2 == "NADA":
            item2 = input("digite somente o item que deseja adicionar: ")
            quantidade2 = int(input("agora digite a quantidade que deseja adicionar: "))
            print("ok",quantidade2,item2,"foi adicionado")
        elif item3 == "NADA":
            item3 = input("digite somente o item que deseja adicionar: ")
            quantidade3 = int(input("agora digite a quantidade que deseja adicionar: "))
            print("ok",quantidade3,item3,"foi adicionado")
        elif item4 == "NADA":
            item4 = input("digite somente o item que deseja adicionar: ")
            quantidade4 = int(input("agora digite a quantidade que deseja adicionar: "))
            print("ok",quantidade4,item4,"foram adicionados")
        elif item5 == "NADA":
            item5 = input("digite somente o item que deseja adicionar: ")
            quantidade5 = int(input("digite a quantidade que deseja adicionar: "))
            print("ok",quantidade5,item5,"foi adicionado")
        else:
            print("opaa, calma ai amigao.. seu limite foi atingido! se quiser mais limite, adquira-a versao premium do site!")
    elif oqfazer == "REMOVER" or oqfazer == "remover" or oqfazer == "Remover" or oqfazer == "remover" or oqfazer == "REMOVER":
        if item5 != "NADA":
            print("seu estoque atualmente é",item1,item2,item3,item4,item5)
            retirar5 = input("qual deseja retirar: ")
            if retirar5 == item1:
                print(item1,"foi removido")
                item1 = "NADA"
                quantidade1 =0
            elif retirar5 == item2:
                print(item2,"foi removido")
                item2 ="NADA"
                quantidade2 = 0
            elif retirar5 == item3:
                print(item3,"foi removido")
                item3 = "NADA"
                quantidade3 = 0
            elif retirar5 == item4:
                print(item4,"foi removido")
                item4 = "NADA"
                quantidade4 = 0
            elif retirar5 == item5:
                print(item5,"foi removido")
                item5 = "NADA"
                quantidade5 =0
        elif item4 != "NADA":
            print("seu estoque atualmente é",item1,item2,item3,item4)
            retirar4 = input("qual deseja retirar: ")
            if retirar4 == item1:
                print(item1,"foi removido")
                item1 = "NADA"
                quantidade1 = 0
            elif retirar4 == item2:
                print(item2,"foi removido")
                item2 = "NADA"
                quantidade2 = 0
            elif retirar4 == item3:
                print(item3,"foi removido")
                item3 = "NADA"
                quantidade3 = 0
            elif retirar4 == item4:
                print(item4,"foi removido")
                item4 = "NADA"
                quantidade4 = 0
        elif item3 != "NADA":
            print("seu estoque atualmente é",item1,item2,item3)
            retirar3 = input("qual deseja retirar: ")
            if retirar3 == item1:
                print(item1,"foi removido")
                item1 = "NADA"
                quantidade1 = 0
            elif retirar3 == item2:
                print(item2,"foi removido")
                item2 ="NADA"
                quantidade2 = 0
            elif retirar3 == item3:
                print(item3,"foi removido")
                item3 = "NADA"
                quantidade3 = 0
        elif item2 != "NADA":
            print("seu estoque atualmente é",item1,item2)
            retirar2 = input("qual deseja retirar: ")
            if retirar2 == item1:
                quantidade1 = 0
                print(item1,"foi removido")
                item1 = "NADA"
            elif retirar2 == item2:
                print(item2,"foi removido")
                item2 ="NADA"
                quantidade2 = 0
        elif item1 != "NADA":
            print("voce só tem ",item1,"no estoque")
            itienes1 = input("deseja remover?")
            if itienes1 == "sim" or itienes1 == "SIM" or itienes1 == "Sim":
                item1 = "NADA"
                quantidade1 = 0
        else:
            print("voce nao tem nada para remover!")
    elif oqfazer == "ver" or oqfazer == "VER" or oqfazer == "Ver":
        if item5 != "NADA":
            print("Seu estoque atualmente é: ", "(1)",item1,":", quantidade1," (2)", item2,":", quantidade2," (3)", item3,":", quantidade3," (4)", item4,":", quantidade4," (5)", item5,":", quantidade5)
        elif item4 != "NADA":
            print("Seu estoque atualmente é: ", "(1)",item1,":", quantidade1," (2)", item2,":", quantidade2,"(3)", item3,":", quantidade3, "(4)",item4,":", quantidade4)
        elif item3 != "NADA":
            print("Seu estoque atualmente é: ", "(1)",item1,":", quantidade1," (2)", item2,":" ,quantidade2," (3)", item3,":",quantidade3)
        elif item2 != "NADA":
            print("Seu estoque atualmente é: ", "(1)",item1,":", quantidade1," (2)",item2, ":",quantidade2)
        elif item1 != "NADA":
            print("Seu estoque atualmente é: ", "(1)",item1,":", quantidade1)
        else:
            print("Seu estoque está atualmente vazio..")
    elif oqfazer == "MUDARQUANTIDADE" or oqfazer == "Mudar Quantidade" or oqfazer == "mudar quantidade" or oqfazer == "mudarquantidade":
        if item5 != "NADA":
            print("Seu estoque atualmente é: ", item1, quantidade1, item2, quantidade2, item3, quantidade3, item4, quantidade4, item5, quantidade5)
            pergunta1 = input("digite qual item voce deseja mudar a quantidade:")
            if pergunta1 == item1:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade1 += pergunta3
                    print("Sua atual quantidade é", quantidade1)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover" or pergunta2 == "remove" or pergunta2 == "Remove":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade1 = quantidade1 - pergunta3
                    print("Sua atual quantidade é", quantidade1)
            elif pergunta1 == item2:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade2 += pergunta3
                    print("Sua atual quantidade é", quantidade2)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade2 = quantidade2 - pergunta3
                    print("Sua atual quantidade é", quantidade2)
            elif pergunta1 == item3:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade3 += pergunta3
                    print("Sua atual quantidade é", quantidade3)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade3 = quantidade3 - pergunta3
                    print("Sua atual quantidade é", quantidade3)
            elif pergunta1 == item4:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade4 += pergunta3
                    print("Sua atual quantidade é", quantidade4)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade4 = quantidade4 - pergunta3
                    print("Sua atual quantidade é", quantidade4)
            elif pergunta1 == item5:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade5 += pergunta3
                    print("Sua atual quantidade é", quantidade5)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade5 = quantidade5 - pergunta3
                    print("Sua atual quantidade é", quantidade5)
        elif item4 != "NADA":
            print("Seu estoque atualmente é: ", item1, quantidade1, item2, quantidade2, item3, quantidade3, item4, quantidade4)
            pergunta1 = input("digite qual item voce deseja mudar a quantidade:")
            if pergunta1 == item1:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade1 += pergunta3
                    print("Sua atual quantidade é", quantidade1)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade1 = quantidade1 - pergunta3
                    print("Sua atual quantidade é", quantidade1)
            elif pergunta1 == item2:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade2 += pergunta3
                    print("Sua atual quantidade é", quantidade2)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade2 = quantidade2 - pergunta3
                    print("Sua atual quantidade é", quantidade2)
            elif pergunta1 == item3:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade3 += pergunta3
                    print("Sua atual quantidade é", quantidade3)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade3 = quantidade3 - pergunta3
                    print("Sua atual quantidade é", quantidade3)
            elif pergunta1 == item4:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade4 += pergunta3
                    print("Sua atual quantidade é", quantidade4)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade4 = quantidade4 - pergunta3
                    print("Sua atual quantidade é", quantidade4)
        elif item3 != "NADA":
            print("Seu estoque atualmente é: ", item1, quantidade1, item2, quantidade2, item3, quantidade3)
            pergunta1 = input("Digite qual item voce deseja mudar a quantidade:")
            if pergunta1 == item1:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade1 += pergunta3
                    print("Sua atual quantidade é", quantidade1)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade1 = quantidade1 - pergunta3
                    print("Sua atual quantidade é", quantidade1)
            elif pergunta1 == item2:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade2 += pergunta3
                    print("Sua atual quantidade é", quantidade2)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade2 = quantidade2 - pergunta3
                    print("Sua atual quantidade é", quantidade2)
            elif pergunta1 == item3:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade3 += pergunta3
                    print("Sua atual quantidade é", quantidade3)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade3 = quantidade3 - pergunta3
                    print("Sua atual quantidade é", quantidade3)
        elif item2 != "NADA":
            print("Seu estoque atualmente é: ", item1, quantidade1, item2, quantidade2)
            pergunta1 = input("Qual item voce deseja mudar a quantidade:")
            if pergunta1 == item1:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade1 += pergunta3
                    print("Sua atual quantidade é", quantidade1)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade1 = quantidade1 - pergunta3
                    print("Sua atual quantidade é", quantidade1)
            elif pergunta1 == item2:
                pergunta2 = input("Voce deseja adicionar ou remover?")
                if pergunta2 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                    pergunta3 = int(input("Quanto voce deseja adicionar"))
                    quantidade2 += pergunta3
                    print("Sua atual quantidade é", quantidade2)
                elif pergunta2 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                    pergunta3 = int(input("Quanto voce deseja remover"))
                    quantidade2 = quantidade2 - pergunta3
                    print("Sua atual quantidade é", quantidade2)
        elif item1 != "NADA":
            print("Seu estoque atualmente é: ", item1, quantidade1)
            pergunta1 = input("voce deseja adicionar ou remover:")
            if pergunta1 == "adicionar" or pergunta1 == "ADICIONAR" or pergunta1 == "Adicionar":
                pergunta3 = int(input("Quanto voce deseja adicionar:"))
                quantidade1 = quantidade1 + pergunta3
                print("Sua atual quantidade é", quantidade1)
            elif pergunta1 == "remover" or pergunta2 == "REMOVER" or pergunta2 == "Remover":
                pergunta3 = int(input("Quanto voce deseja remover:"))
                quantidade1 = quantidade1 - pergunta3
                print("Sua atual quantidade é", quantidade1)
        else:
            print("só peço que escreve de forma compreensivel pois ate mesmo eu preciso entender")
    elif oqfazer == fecho:
        print("Seu estoque foi temporariamente fechado. Reinicie o programa para inicia-lo novamente.")
        break

    else:
        print("opçao invalida. tente novamente")