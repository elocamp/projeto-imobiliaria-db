import functions.insert_data
import functions.get_data
import functions.delete_data
import functions.export_db

def exibir_menu():
    print("""Aplicação de Cadastro Imobiliário
          
          1 - Adicionar um novo registro
          2 - Listar dados de um apartamento
          3 - Listar todos os registros
          4 - Remover um registro
          5 - Exportar dados para Excel
          0 - Encerrar a aplicação\n""")

def processar_escolha(opcao):
    if opcao == 1:
        cliente_nome = input("Insira o nome do cliente: ")
        cliente_sobrenome = input("Insira o sobrenome do cliente: ")
        cliente_cpf = input("Insira o CPF do cliente: ")
        cliente_telefone = input("Insira o telefone do cliente: ")
        
        
        print("Informações do apartamento\n")
        apartamento_numero = input("Insira o número do apartamento: ")
        apartamento_andar = str(apartamento_numero[0])
        apartamento_bloco = input("Insira o bloco do apartamento: ")
        apartamento_valor = float(input("Insira o valor do apartamento: "))
        
        print("Informações da vaga da garagem\n")
        carro_placa = input("Insira a placa do carro: ")
        carro_marca = input("Insira a marca do carro: ")
        carro_modelo = input("Insira o modelo do carro: ")
        carro_cor = input("Insira a cor do carro: ")
        
        functions.insert_data.add_cliente('dados_imobiliaria.db', int(apartamento_numero), cliente_nome, cliente_sobrenome, cliente_cpf, cliente_telefone)
        functions.insert_data.add_apartamento('dados_imobiliaria.db', int(apartamento_numero), int(apartamento_andar), apartamento_bloco, apartamento_valor)
        functions.insert_data.add_vaga('dados_imobiliaria.db', apartamento_numero, carro_placa, carro_marca, carro_modelo, carro_cor)
        
        print("\nRegistro adicionado com sucesso!\n")
        
    elif opcao == 2:
        ap = int(input("Insira o apartamento desejado para retornar as informações: "))
        data_cliente = functions.get_data.get_data_cliente('dados_imobiliaria.db', ap)
        data_apartamento = functions.get_data.get_data_apartamento('dados_imobiliaria.db', ap)
        data_vaga = functions.get_data.get_data_vaga('dados_imobiliaria.db', ap)
        
        print(data_cliente)
        print(data_apartamento)
        print(data_vaga)
    
    elif opcao == 3:
        print(functions.get_data.get_table('dados_imobiliaria.db', 'clientes'))
        print(functions.get_data.get_table('dados_imobiliaria.db', 'apartamentos'))
        print(functions.get_data.get_table('dados_imobiliaria.db', 'vagas_garagem'))
    
    elif opcao == 4:
        ap = int(input("Insira o apartamento desejado para retornar as informações: "))
        functions.delete_data.delete_cliente('dados_imobiliaria.db', ap)
        functions.delete_data.delete_apartamento('dados_imobiliaria.db', ap)
        functions.delete_data.delete_vaga_garagem('dados_imobiliaria.db', ap)
        
        print("Registro apagado com sucesso.\n")
    
    elif opcao == 5:
        functions.export_db.export_all_data()
        print("Os dados foram exportados com sucesso.\n")
    
    elif opcao == 0:
        print("\nPrograma encerrado!\n")
        
    
    else:
        print("Opção inválida. Tente novamente.")