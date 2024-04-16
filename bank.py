def format_output(message):
    print("\n" + "RESULTADO".center(50, "="))
    print(message)
    print("=" * 50)

def sacar(saldo, extrato, saques_feitos, valor_limite_saque, qtde_limite_saque):
    if saques_feitos >= qtde_limite_saque:
        format_output("Limite diário de saques atingido")
        return saldo, extrato, saques_feitos
    
    saque = float(input("Valor do saque: R$ "))
    if saque <= 0:
        format_output("Valor do saque deve ser maior que zero!")
    elif saque > saldo:
        format_output("Saldo insuficiente!")
    elif saque > valor_limite_saque:
        format_output(f"Limite de saque diário: R$ {valor_limite_saque}")
    else:
        saldo -= saque
        extrato += f"\nSaque: R$ {saque:.2f}\n"
        format_output(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        saques_feitos += 1
    
    return saldo, extrato, saques_feitos

def depositar(valor, extrato, saldo):
    if valor <= 0:
        format_output("Valor do depósito deve ser maior que zero!")
    else:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"
        format_output(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    return saldo, extrato

def exibir_extrato(extrato, saldo):
    print("=" * 50)
    print("EXTRATO".center(50))
    print("=" * 50)
    print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=" * 50)

def criar_usuario(lista_clientes):
    cpf = input("Digite seu CPF: ")
    if any(c["CPF"] == cpf for c in lista_clientes):
        format_output("CPF já cadastrado!")
    else:
        nome = input("Nome completo: ")
        nascimento = input("Data de nascimento (ex: xx/xx/xxxx): ")
        endereco = input("Endereço (ex: logradouro, nro, bairro, cidade, estado): ")
        endereco = ", ".join([item.strip() for item in endereco.split(",")])
        lista_clientes.append({"nome": nome, "nascimento": nascimento, "CPF": cpf, "endereco": endereco})
        format_output("Usuário criado com sucesso!")
    return lista_clientes

def criar_conta(lista_clientes, contas_existentes):
    cpf = input("Digite seu CPF: ")
    cliente = next((c for c in lista_clientes if c["CPF"] == cpf), None)
    if cliente is None:
        format_output("CPF não encontrado!")
        return contas_existentes
    
    if contas_existentes:
        ultimo_numero_conta = max(c[1] for c in contas_existentes)
        nova_conta = (cliente["CPF"], ultimo_numero_conta + 1, cliente["nome"])
    else:
        nova_conta = (cliente["CPF"], 1, cliente["nome"])

    contas_existentes.append(nova_conta)
    format_output("Conta criada com sucesso!")
    return contas_existentes

def exibir_clientes_cadastrados(lista_clientes):
    if not lista_clientes:
        format_output("Não há clientes cadastrados.")
    else:
        print("=" * 50)
        print("CLIENTES CADASTRADOS".center(50))
        print("=" * 50)
        for cliente in lista_clientes:
            print(f"Nome: {cliente['nome']}\nCPF: {cliente['CPF']}\nEndereço: {cliente['endereco']}\n")
        print("=" * 50)

def exibir_contas_cadastradas(contas_existentes):
    if not contas_existentes:
        format_output("Não há contas cadastradas.")
    else:
        print("=" * 50)
        print("CONTAS CADASTRADAS".center(50))
        print("=" * 50)
        for conta in contas_existentes:
            print(f"CPF: {conta[0]}\nNúmero: {conta[1]}\nTitular: {conta[2]}\n")
        print("=" * 50)

def menu():
    print("\n" + "=" * 50)
    print("BANCO XYZ".center(50))
    print("=" * 50)
    print("1. Depositar\n2. Sacar\n3. Extrato\n4. Criar Usuário\n5. Criar Conta\n6. Exibir Usuários Cadastrados\n7. Exibir Contas Cadastradas\n8. Sair")

def main():
    VALOR_LIMITE_SAQUE = 500
    QTDE_LIMITE_SAQUE = 3
    saldo = 0.0
    extrato = "Extrato de hoje:\n"
    saques_feitos = 0
    lista_clientes = []
    contas_existentes = []

    while True:
        menu()
        option = input("Escolha uma opção: ")
        if option == "1":
            saldo, extrato = depositar(float(input("Valor do depósito: R$ ")), extrato, saldo)
        elif option == "2":
            saldo, extrato, saques_feitos = sacar(saldo, extrato, saques_feitos, VALOR_LIMITE_SAQUE, QTDE_LIMITE_SAQUE)
        elif option == "3":
            exibir_extrato(extrato, saldo)
        elif option == "4":
            lista_clientes = criar_usuario(lista_clientes)
        elif option == "5":
            contas_existentes = criar_conta(lista_clientes, contas_existentes)
        elif option == "6":
            exibir_clientes_cadastrados(lista_clientes)
        elif option == "7":
            exibir_contas_cadastradas(contas_existentes)
        elif option == "8":
            format_output("Obrigado por usar o Banco XYZ. Volte sempre!")
            break
        else:
            format_output("Opção inválida! Escolha novamente.")

main()
