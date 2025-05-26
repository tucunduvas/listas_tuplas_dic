carrinho = {}
while True:
    print("carinho de compras")
    print("adiconar items")
    print("remover items")
    print("total de items")
    print("para parar o menu, digite finalizar")

    acao = input("qual ação deseja realizar: ").lower()
    
    if acao == 'adicionar':
        while True: 
            item = input("qual item deseja adiconar, para sair digite sair: ")
            if item == 'sair':
                break
            preco = float(input("insira o valor desse item: "))
            carrinho[item] = preco
    
    if acao == 'remover':
        while True: 
            remocao = input("qual item deseja remover?, para sair digite sair: ")
            if remocao == 'sair':
                break
            if remocao in carrinho:
                del carrinho[remocao]
            else:
                print("o item que quer remover não existe")
                
    if acao == 'total':
        for elementos in carrinho.items():
            print(elementos)
                
    if acao == 'finalizar':
        break
    else:
        print("ação inválida")