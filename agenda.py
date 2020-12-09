AGENDA ={}


def mostrar_contatos():
   if AGENDA:
       for contato in AGENDA:
           buscar_contato(contato)
       print('***************')
   else:
       print('Agenda vazia')

def buscar_contato(contato):
    try:
        print('***************')
        print('Nome:', contato)
        print('telefone:', AGENDA[contato]['telefone'])
        print('Email:', AGENDA[contato]['email'])
        print('Endereço:', AGENDA[contato]['endereco'])
    except KeyError:
        print('>>>>contato inexistente')
    except Exception as error:
        print('>>> Um erro inesperado ocorreu')
        print(error)

def ler_detalhes_contato():
    telefone = int(input('Digite o telefone do contato:'))
    email = str(input('Digite o email do contato:'))
    endereco = str(input('Digite o endereco do contato:'))
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print('>>>> Contato {} adicionado/editado com sucesso'.format(contato))
    print()



def excluir_contato(contato):
   try:
        AGENDA.pop(contato)
        salvar()
        print('>>>>>contato {} excluido com sucesso!'.format(contato))
   except KeyError:
        print('>>>>contato inexistente')
   except Exception as error:
       print('>>> Um erro inesperado ocorreu')

       print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('>>>> Agenda exportada com sucesso')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos')
        print(error)

def importar_contato(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>>>>Arquivo não encontrado')
    except Exception as error:
        print('>>>>Algum erro inesperado ocorreu')
        print(error)
def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>>>Database carregado com sucesso!')
    except FileNotFoundError:
        print('>>>>>Arquivo não encontrado')
    except Exception as error:
        print('>>>>Algum erro inesperado ocorreu')
        print(error)

def imprimir_menu():
    print('__________________________________________')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contatos da agenda')
    print('4 - Editar contatos da agenda')
    print('5 - Excluir contatos da agenda')
    print('6 - Exportar contatos')
    print('7 - Importar Contatos')
    print('8 - Fechar agenda')
    print('__________________________________________')


carregar()
while True:

    imprimir_menu()
    opcao = input('Digite uma opção:')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato:')
        buscar_contato(contato)
    elif opcao == '3':
        contato = str(input('Digite o nome do contato:'))
        try:
            AGENDA[contato]
            print('>>>>>>Contato ja existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = str(input('Digite o nome do contato:'))
        try:
            AGENDA[contato]
            print('>>>>>>Editando contato:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>>>>>Contato Inexistente')

    elif opcao == '5':
        contato = input('Digite o nome do contato:')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado:')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado:')
        importar_contato(nome_do_arquivo)
    elif opcao == '8':
        print('Fechando programa')
        break
    else:
        print('Opcao Invalida!')
