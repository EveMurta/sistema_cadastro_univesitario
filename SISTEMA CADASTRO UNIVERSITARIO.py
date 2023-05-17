# EVELINE AMORIM MURTA - ANALISE E DESENVOLVIMENTO DE SISTEMAS

#Importa arquivo JSON
import json

# Variaveis
lista_qualquer = []
num_menu = ["0","ESTUDANTE","PROFESSOR","DISCIPLINA","TURMA","MATRICULA"]
menu2 = []

# Funcao que imprime menu principal
def imprime_menu_principal():

    print(f'\n{"--- MENU PRINCIPAL ---":^26}')
    print("(1) Gerenciar estudantes")
    print("(2) Gerenciar professores")
    print("(3) Gerenciar disciplinas")
    print("(4) Gerenciar turmas")
    print("(5) Gerenciar matriculas")
    print("(6) Sair")

    #Recebe dado da opcao de menu do usuario
    return int(input("Digite o número correspondente a opção desejada: "))

#Funcao que imprime menu secundario
def imprime_menu_opcional():

    print("\n--- GERENCIAR",num_menu[menu1]," ---")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(5) Voltar ao menu principal")
    return int(input("Digite o número correspondente a opção desejada: "))


#Funcao laco de repeticao para solicitacao de dados e inclusao na lista
def solicitar_dados(lista_qualquer):

   if menu1 <= 2:
       while True:
          for i in range(1):

            #Variaveis de entrada

            codigo1 = int(input("\nDigite o código do(a) "f'{num_menu[menu1]}'": "))
            nome1 = str(input("Digite o nome do(a) "f'{num_menu[menu1]}'": "))
            cpf1 = int(input("Digite o CPF do(a) "f'{num_menu[menu1]}'": "))
            novo = {"Codigo": codigo1, "Nome": nome1,"CPF": cpf1}

            #condicao para salvar na lista certa:
            if menu1 == 1:
                #Le o arquivo JSON
                lista_qualquer = ler_arquivo("estudante.json")
                #Adicao dos dados `a lista
                lista_qualquer.append(novo)
                # funcao salvar aqruivo
                salvar_arquivo(lista_qualquer, "estudante.json")

                #Loop
                if input(str("\n"f'{num_menu[menu1]}'" adicionado(a)! Deseja cadastrar outro(a)? (s/n): \n")) == "s":
                    continue
                else:
                    return

            else:
                if menu1 == 2:
                    # Le o arquivo JSON
                    lista_qualquer = ler_arquivo("professor.json")
                    # Adicao dos dados `a lista
                    lista_qualquer.append(novo)
                    # funcao salvar aqruivo
                    salvar_arquivo(lista_qualquer, "professor.json")

                    #Loop
                    if input(str("\n"f'{num_menu[menu1]}'" adicionado(a)! Deseja cadastrar outro(a)? (s/n): \n")) == "s":
                        continue
                    else:
                        return
                else:
                    print("\nArquivo NAO salvo!")




   elif menu1 >2 and menu1 <6 :
       for i in range(1):

           if menu1 == 3:
               # Variaveis de entrada
               codigo1 = int(input("\nDigite o código do(a) "f'{num_menu[menu1]}'": "))
               nome1 = str(input("Digite o nome da "f'{num_menu[menu1]}'": "))
               novo = {"Codigo": codigo1, "Nome": nome1}
               # Le o arquivo JSON
               lista_qualquer = ler_arquivo("disciplina.json")
               # Adicao dos dados `a lista
               lista_qualquer.append(novo)
               # funcao salvar aqruivo
               salvar_arquivo(lista_qualquer, "disciplina.json")
           else:
               if menu1 == 4:
                   # Variaveis de entrada
                   codigo = int(input("\nDigite o código da "f'{num_menu[menu1]}'": "))
                   codigo_professor = int(input("Digite o código do professor: "))
                   codigo_disciplina = int(input("Digite o código da disciplina: "))

                   novo = {"Codigo": codigo, "Codigo_Professor": codigo_professor,
                           "Codigo_Disciplina": codigo_disciplina}
                   # Le o arquivo JSON
                   lista_qualquer = ler_arquivo("turma.json")
                   # Adicao dos dados `a lista
                   lista_qualquer.append(novo)
                   # funcao salvar aqruivo
                   salvar_arquivo(lista_qualquer, "turma.json")
               else:
                   if menu1 == 5:
                       # Variaveis de entrada
                       codigo_turma = int(input("\nDigite o código da turma: "))
                       codigo_estudante = int(input("Digite o código do estudante: "))

                       novo = {"Codigo_turma": codigo_turma, "Codigo_estudante": codigo_estudante}

                       # Le o arquivo JSON
                       lista_qualquer = ler_arquivo("matricula.json")
                       # Adicao dos dados `a lista
                       lista_qualquer.append(novo)
                       # funcao salvar aqruivo
                       salvar_arquivo(lista_qualquer, "matricula.json")
                   else:
                       print("\nArquivo NAO salvo!")

           if input("\n"f'{num_menu[menu1]}'" adicionado(a)! Deseja cadastrar outro(a)? (s/n): \n") == "s":
               continue

           else:
               return


#Funcao laco de repeticao para impressao do dicionario
def listar(lista_qualquer):

    print("\n--- LISTAR "f'{num_menu[menu1]}'" ---")

    if menu1 == 1:
        lista_qualquer = ler_arquivo("estudante.json")

        for estudante in lista_qualquer:
            print("Dados do "f'{num_menu[menu1]}'": "f'{estudante}')
    else:
        if menu1 == 2:
            lista_qualquer = ler_arquivo("professor.json")

            for i in lista_qualquer:
                print("Dados do "f'{num_menu[menu1]}'": "f'{i}')
        else:
            if menu1 == 3:
                lista_qualquer = ler_arquivo("disciplina.json")

                for i in lista_qualquer:
                    print("Dados do "f'{num_menu[menu1]}'": "f'{i}')
            else:
                if menu1 == 4:
                    lista_qualquer = ler_arquivo("turma.json")

                    for i in lista_qualquer:
                       print("Dados do "f'{num_menu[menu1]}'": "f'{i}')
                else:
                    if menu1 == 5:
                        lista_qualquer = ler_arquivo("matricula.json")

                        for i in lista_qualquer:
                            print("Dados dq "f'{num_menu[menu1]}'": "f'{i}')
                    else:
                        print("Nada cadastrado!")



#Funcao de editar dados
def editar(codigo, lista_qualquer):

    if menu1 == 1:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("estudante.json")
        #Percorrer a lista para encontrar o codigo
        for estudante in lista_qualquer:
            if codigo == estudante["Codigo"]:
                # Variaveis de entrada estudante
                estudante["Nome"] = str(input("Digite o novo nome: "))
                estudante["CPF"] = int(input("Digite o novo CPF: "))
                print("Estudante atualizado!")


                #salva arquivo
                salvar_arquivo(lista_qualquer, "estudante.json")

                return
    elif menu1 == 2:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("professor.json")
        # Percorrer a lista para encontrar o codigo
        for professor in lista_qualquer:

            if professor["Codigo"] == codigo:
                # Variaveis de entrada
                professor["Nome"] = str(input("Digite o novo nome: "))
                professor["CPF"] = int(input("Digite o novo CPF: "))
                print("Professor atualizado!")

                # salva arquivo
                salvar_arquivo(lista_qualquer, "professor.json")
                return
    elif menu1 == 3:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("disciplina.json")
        # Percorrer a lista para encontrar o codigo
        for disciplina in lista_qualquer:
            if disciplina["Codigo"] == codigo:
                # Variaveis de entrada
                disciplina["Nome"] = str(input("Digite o novo nome: "))
                print("Disciplina atualizada!")

                # salva arquivo
                salvar_arquivo(lista_qualquer, "disciplina.json")

                return
    elif menu1 == 4:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("turma.json")
        #Percorrer a lista para encontrar o codigo
        for turma in lista_qualquer:
            if turma["Codigo"] == codigo:
                # Variaveis de entrada
                turma["Codigo_professor"] = str(input("Digite o novo codigo do Professor: "))
                turma["Codigo_disciplina"] = str(input("Digite o novo codigo da Disciplina: "))

                print("Turma atualizada!")

                # salva arquivo
                salvar_arquivo(lista_qualquer, "turma.json")

                return
    elif menu1 == 5:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("matricula.json")
        #Percorrer a lista para encontrar o codigo
        for matricula in lista_qualquer:
            if matricula["Codigo_turma"] == codigo:
                # Variaveis de entrada
                matricula["Codigo_estudante"] = str(input("Digite o novo estudante: "))

                print("Matricula atualizada!")

                # salva arquivo
                salvar_arquivo(lista_qualquer, "matricula.json")

                return

#Funcao para excluir itens
def excluir(codigo, lista_qualquer):

    #variavel de remocao
    remover = None

    if menu1 == 1:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("estudante.json")
        #Percorre a lista e define o estudante a ser removido
        for estudante in lista_qualquer:
            if estudante["Codigo"] == codigo:
                remover = estudante

                break
        #Exclui o estudante
        if remover is not None:
            lista_qualquer.remove(remover)
            salvar_arquivo(lista_qualquer, "estudante.json")

            print("Estudante excluido!")
        else:
            print("Codigo nao encontradao!")

    elif menu1 == 2:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("professor.json")
        # Percorre a lista e define o professor a ser removido
        for professor in lista_qualquer:
            if professor["Codigo"] == codigo:
                remover = professor

                break
        # Exclui o professor
        if remover is not None:
            lista_qualquer.remove(remover)
            salvar_arquivo(lista_qualquer, "professor.json")


            print("Professor excluido!")
        else:
            print("Codigo nao encontradao!")

    elif menu1 == 3:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("disciplina.json")
        # Percorre a lista e define a disciplina a ser removida
        for disciplina in lista_qualquer:
            if disciplina["Codigo"] == codigo:
                remover = disciplina

                break
        # Exclui a disciplina
        if remover is not None:
            lista_qualquer.remove(remover)
            salvar_arquivo(lista_qualquer, "disciplina.json")


            print("Disciplina excluida!")
        else:
            print("Codigo nao encontradao!")

    elif menu1 == 4:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("turma.json")
        # Percorre a lista e define a turma a ser removida
        for turma in lista_qualquer:
            if turma["Codigo"] == codigo:
                remover = turma

                break
        # Exclui a turma
        if remover is not None:
            lista_qualquer.remove(remover)
            salvar_arquivo(lista_qualquer, "turma.json")


            print("Turma excluida!")
        else:
            print("Codigo nao encontradao!")

    elif menu1 == 5:
        # Le o arquivo JSON
        lista_qualquer = ler_arquivo("matricula.json")
        # Percorre a lista e define a matricula a ser removido
        for matricula in lista_qualquer:
            if matricula["Codigo_turma"] == codigo:
                remover = matricula

                break
        # Exclui a matricula
        if remover is not None:
            lista_qualquer.remove(remover)
            salvar_arquivo(lista_qualquer, "matricula.json")


            print("Matricula excluida!")
        else:
            print("Codigo nao encontradao!")

#Funcao para salvar como arquivo JSON:
def salvar_arquivo(lista_qualquer, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo_aberto:
        json.dump(lista_qualquer, arquivo_aberto, ensure_ascii=False)

#Funcao para ler arquivo JSON:
def ler_arquivo(nome_arquivo):
    #comando para tentar ler arquivo
    try:
        with open(nome_arquivo,'r', encoding='utf8') as arquivo_aberto:
            lista_qualquer = json.load(arquivo_aberto)

        return lista_qualquer
    #caso nao leia retorne lista vazia
    except:
        return []

#loop do menu principal
while True:

    #imprime menu principal e retorna variavel de opcao de menu
    menu1 = imprime_menu_principal()

    #Condicional de selecao de opcao 1 do menu
    if(menu1 == 1):
        #Loop do menu estudantes
        while True:
            menu2 = imprime_menu_opcional()

            #Condicional para opcao 1 do menu de estudantes
            if (menu2 == 1):
                    solicitar_dados(lista_qualquer)

            else:
                #Opcao 2 do menu estudantes, impressao da tupla
                if (menu2 == 2):
                    listar(lista_qualquer)
                    break

                else:
                    #Opcao 3 do menu de estudantes
                    if (menu2 == 3):
                        # Pedindo o dado a ser alterado
                        print("\n")
                        codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja editar: "))
                        editar(codigo, lista_qualquer)

                    else:
                        #Opcao 4 do menu de estudantes
                        if (menu2 == 4):
                            # Pedindo codigo do item a ser excluido
                            print("--- EXCLUIR "f'{num_menu[1]}'" ---")
                            codigo = int(input("Digite o codigo de "f'{num_menu[1]}'" que deseja excluir: "))
                            excluir(codigo, lista_qualquer)
                        else:
                            break

    else:
         #Condicional de selecao de opcao 2 do menu
        if(menu1 == 2):
            # Loop do menu professores
            while True:
                menu2 = imprime_menu_opcional()
                # Condicional para opcao 1 do menu de professores
                if (menu2 == 1):
                        solicitar_dados(lista_qualquer)
                else:
                    # Opcao 2 do menu professores, impressao da lista
                    if (menu2 == 2):
                        listar(lista_qualquer)

                    else:
                        # Opcao 3 do menu de professores
                        if (menu2 == 3):
                            # Pedindo o dado a ser alterado
                            print("\n")
                            codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja editar: "))
                            editar(codigo, lista_qualquer)

                        else:
                            # Opcao 4 do menu de professores
                            if (menu2 == 4):
                                # Pedindo codigo do item a ser excluido
                                print("\n--- EXCLUIR "f'{num_menu[menu1]}'" ---")
                                codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja excluir: "))
                                excluir(codigo, lista_qualquer)
                            else:
                                break
        else:
            # Opcao 3 do menu de principal
            if(menu1 == 3):
                # Loop de menu
                while True:
                    menu2 = imprime_menu_opcional()
                    # Condicional para opcao 1 do menu de disciplinas
                    if (menu2 == 1):
                            solicitar_dados(lista_qualquer)
                    else:
                        # Opcao 2 do menu disciplinas, impressao da lista
                        if (menu2 == 2):
                            listar(lista_qualquer)

                        else:
                            # Opcao 3 do menu de disciplinas
                            if (menu2 == 3):
                                # Pedindo o dado a ser alterado
                                print("\n")
                                codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja editar: "))
                                editar(codigo, lista_qualquer)

                            else:
                                # Opcao 4 do menu de disciplinas
                                if (menu2 == 4):
                                    # Pedindo codigo do item a ser excluido
                                    print("\n--- EXCLUIR "f'{num_menu[menu1]}'" ---")
                                    codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja excluir: "))
                                    excluir(codigo, lista_qualquer)
                                else:
                                    break
            else:
                # Opcao 4 do menu de principal
                if (menu1 == 4):
                    # Loop de menu
                    while True:
                        menu2 = imprime_menu_opcional()
                        # Condicional para opcao 1 do menu de turmas
                        if (menu2 == 1):
                                solicitar_dados(lista_qualquer)

                        else:
                            # Opcao 2 do menu turma, impressao da lista
                            if (menu2 == 2):
                                listar(lista_qualquer)

                            else:
                                # Opcao 3 do menu de turmas
                                if (menu2 == 3):
                                    # Pedindo o dado a ser alterado
                                    print("\n")
                                    codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja editar: "))
                                    editar(codigo, lista_qualquer)

                                else:
                                    # Opcao 4 do menu de turmas
                                    if (menu2 == 4):
                                        # Pedindo codigo do item a ser excluido
                                        print("\n--- EXCLUIR "f'{num_menu[menu1]}'" ---")
                                        codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja excluir: "))
                                        excluir(codigo, lista_qualquer)
                                    else:
                                        break

                else:
                    if (menu1 == 5):
                        # Loop de menu
                        while True:
                            menu2 = imprime_menu_opcional()
                            # Condicional para opcao 1 do menu de matriculas
                            if (menu2 == 1):
                                    solicitar_dados(lista_qualquer)
                            else:
                                # Opcao 2 do menu matriculas, impressao da lista
                                if (menu2 == 2):
                                    listar(lista_qualquer)

                                else:
                                    # Opcao 3 do menu de matriculas
                                    if (menu2 == 3):
                                        # Pedindo o dado a ser alterado
                                        print("\n")
                                        codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja editar: "))
                                        editar(codigo, lista_qualquer)

                                    else:
                                        # Opcao 4 do menu de matriculas
                                        if (menu2 == 4):
                                            # Pedindo codigo do item a ser excluido
                                            print("\n--- EXCLUIR "f'{num_menu[menu1]}'" ---")
                                            codigo = int(input("Digite o codigo de "f'{num_menu[menu1]}'" que deseja excluir: "))
                                            excluir(codigo, lista_qualquer)
                                        else:
                                            break
                    else:
                        #Finalizacao do loop do menu principal
                        if (menu1 == 6):
                           print("\n")
                           print("Até a próxima! :)")
                           break

                        else:
                            print("Ops, essa nao e uma opcao!")
                            menu1 = imprime_menu_principal()


