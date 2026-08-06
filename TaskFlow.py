print("========== TASKFLOW ==========")
tarefas = []
while True:
    print("1- Adicionar tarefa")
    print("2- Listar tarefas")
    print("3- Concluir tarefa")
    print("4- Remover tarefa")
    print("5- Sair")

    opcao = input("Escolha uma opção:")
    if opcao == "1":
        nome_tarefa = str(input("Qual tarefa deseja adicionar?:"))
        if not nome_tarefa:
            print("Nome não pode estar vazio.")
            continue
        tarefa = {"nome": nome_tarefa, "concluida": False}
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa adicionada ainda.")
            continue
        for indice, tarefa in enumerate(tarefas):
           if tarefa["concluida"] == False:
                print(indice + 1, "[ ]", tarefa["nome"])
           else:
               print(indice +1, "[x]", tarefa["nome"])
    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa adicionada ainda.")
            continue
        for indice, tarefa in enumerate(tarefas):
            print(indice + 1, tarefa["nome"])
        try:
            tarefa_concluida = int(input("Qual tarefa deseja concluir?:"))
            if tarefa_concluida < 1 or tarefa_concluida > len(tarefas):
                print("Tarefa não encontrada")
            else:
                tarefas[tarefa_concluida - 1]["concluida"] = True
                print("Tarefa concluída!")
        except ValueError:
            print("Digite uma tarefa válida.")
    elif opcao == "4":
        if not tarefas:
            print("Nenhuma tarefa adicionada ainda.")
            continue
        for indice, tarefa in enumerate(tarefas):
            print(indice + 1, tarefa["nome"])
        try:
            remover_tarefa = int(input("Qual tarefa deseja remover?:"))
            if remover_tarefa < 1 or remover_tarefa > len(tarefas):
                print("Tarefa não encontrada.")
            else:
                nome_da_tarefa = tarefas[remover_tarefa - 1]["nome"]
                confirmar_remover = input(f"Tem certeza de que deseja remover: '{nome_da_tarefa}', (s/n)")
                if confirmar_remover == "s":
                    tarefas.pop(remover_tarefa - 1)
                    print("Tarefa removida com sucesso!")
                elif confirmar_remover == "n":
                    print("Remoção cancelada.")
                continue
        except ValueError:
            print("Insira uma tarefa válida.")
    elif opcao == "5":
        print("Obrigado por usar o TaskFlow.")
        break
    else:
        print("Opção inválida.")
