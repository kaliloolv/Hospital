import cliente as c # importar de um file e nomeiar de c
import medico as b
while True:
    print(" Seja bem-vindo ao The best hospital o brazil!!")
    print("1- cadastrar paciente")
    print("2- cadastrar medico")
    print("3- buscar paciente")
    print("4- buscar medico")
    print("5- Sair")
    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        nome = input("nome: ")
        idade = int(input(" Digite sua idade: "))
        sangue = input("Qual o tipo sanguíneo: ")
        numero = int(input("numero do paciente: "))
        user01= c.paciente(nome,idade,sangue,numero)
        user01.Cadastrarpaciente()
        print("Paciente cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        crm = int(input(" Digite sua crm: "))
        numero = int(input("Digite o telefone para contato: "))
        user02 = b.medico(nome,idade,crm,numero)
        user02.CadastrarMedico()
        print("Médico cadastrado com sucesso!")
    elif opcao == 3:
        nomeBuscado = input("Qual nome você deseja buscar: ")
        dadosEncontradospaciente = user01.Listarpaciente(nomeBuscado)
        print(dadosEncontradospaciente)

    elif opcao == 4:
        nomeBuscado = input("Qual nome você deseja buscar: ")
        dadosEncontradosMedico = user02.ListarMedico(nomeBuscado)
        print(dadosEncontradosMedico)
        print("Médico encontrado com sucesso!!")

    elif opcao == 5:
        print(" Até a próxima!")
        break
#parte 3 ( junção dos 2 mais programa para unir os dois)