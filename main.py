import menu1

while True:
        menu1.exibir_menu()
        escolha = int(input())
        menu1.processar_escolha(escolha)
        
        if escolha == 0:
            break