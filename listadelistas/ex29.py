lista = list()
while True:
    print("Para realizar a ação digite: ") 
    print("ADICIONAR")
    print("REMOVER")
    print("LISTAR")
    print("VOLTAR PARA O MENU")
    print("finalizar, PARA SAIR DO MENU")
    opcao = input("Digite o desejado: ").lower()

    if opcao == 'adicionar':
        print("Adicionando elementos da lista: ")
        while True:
            elementos = input("digite os elementos da lista, para sair digite 'sair': ").lower()
            if elementos == 'sair':
                break
            lista.append(elementos)


    elif opcao == 'remover':
        print("Remoção de elementos da lista: ")
        while True:
            remocao = input("digite quais elementos deseja remover, para sair digite 'sair': ").lower()
            if not lista:
                print("a lista está vazia")
            if remocao == 'sair':
                break
            if remocao in lista:
                lista.remove(remocao)
                print(f"O elemento {remocao} foi removido!")
            else:
                print("elemento nao encontrado")
            # for i in lista:
            #     if remocao == i:
            #         lista.remove(elementos)
            #     else:
            #         print("elemento nao encontrado")
            
            
    elif opcao == 'listar':
        print("Listando elementos da lista: ")
        if lista:
            for i in lista:
                print(i)
        else:
            ("nenhum elemento na lista")
    
    elif opcao == 'finalizar':
        break        
    else: 
        print("Opcão inválida")
