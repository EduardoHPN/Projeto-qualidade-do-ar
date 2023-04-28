import adicionar
import deletar
import classificar
import update
#apresentação doprograma

#repetição
while True:

    #apresentação das opções
    print('\n')
    print('*'*60)
    print('Menu Principal'.center(60))
    print('*'*60)
    print("1- Incluir amostra")
    print("2- Alterar amostra")
    print("3- Excluir amostra")
    print("4- Classificar ar")
    print("5- Sair do Sistema\n")
    
    #entrada da escolha
    pick=input("Escolha a opção que deseja: ")
    
    #resultado da Escolha
    if pick == "1":
        adicionar.adicionar()
    #escolha de numero 2 - alterar
    elif pick =="2":
        update.mudar()           
    #Escolha de numero 3 - excluir
    elif pick =="3":
        deletar.deletar()           
    #escolha de numero 4 - classificar
    elif pick =="4":
        classificar.classificar()
    #escolha de numero 5 - fechar o programa
    elif pick =="5":
        print("Obrigado por usar este programa!")
        break
    else:
        print('digite um valor validos!!')

