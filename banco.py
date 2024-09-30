banco = [
    {
    'numero': 1,
    'nome': 'Luiz',
    'saldo': 300,
    'ativo': True
    },
    {
    'numero': 2,
    'nome': 'Joao',
    'saldo': 0,
    'ativo': True
    }
]
numero_conta = 2

def listar() -> None:
    print('--- CONTAS CADASTRADAS ---')
    for conta in banco:
        print(f"Numero: {conta['numero']}")
        print(f"Nome: {conta['nome']}")
        print(f"Saldo: {conta['saldo']}")
        print(f"Ativo: {conta['ativo']}")
        print('-'*30)

def criarConta(nome: str, ativo: bool = True) -> dict:
    global numero_conta
    numero_conta += 1
    conta = {
        'numero': numero_conta,
        'nome': nome,
        'saldo': 0,
        'ativo': ativo
    }
    return conta

def addConta(nome: str, ativo: bool = True):
    conta = criarConta(nome, ativo)
    banco.append(conta)
    print('Conta cadastrada com sucesso!')

def buscarContaPorNumero(numero:int) -> dict | None:
    for conta in banco:
        if conta['numero'] == numero:
            print(f"Numero: {conta['numero']}")
            print(f"Nome: {conta['nome']}")
            print(f"Saldo: {conta['saldo']}")
            print(f"Ativo: {conta['ativo']}")
            return conta
    print('Conta não encontrada!')
    return None

def deletar(numero:int):
    conta = buscarContaPorNumero(numero)
    if conta:
        banco.remove(conta)
        print('Conta removida com sucesso!')

def editar(numero: int, novo_nome: str):
    conta = buscarContaPorNumero(numero)
    if conta:
        conta['nome'] = novo_nome
        print('Dados alterados com sucesso!')

def ativa(numero: int):
    conta = buscarContaPorNumero(numero)
    if conta:
        conta['ativo'] = True
        print('Conta Ativada!')

def desativar(numero: int):
    conta = buscarContaPorNumero(numero)
    if conta:
        conta['ativo'] = False
        print('Conta Desativada!')

def depositar(numero: int, valor_depositado: float):
    conta = buscarContaPorNumero(numero)
    if conta:
        if valor_depositado <= 0:
            print('Valor de depósito inválido!')
        else:
            conta['saldo'] += valor_depositado
            print(f'O valor de R$ {valor_depositado} foi depositado!')

def sacar(numero: int, saque: float):
    conta = buscarContaPorNumero(numero)
    if conta:
        if not conta['ativo']:
            print('Conta não está ativa!')
            return
        if conta['saldo'] >= saque:
            conta['saldo'] -= saque
            print(f'O valor de R$ {saque} foi sacado!')
        else:
            print('Saldo insuficiente!')

def transferencia(numero: int, valor: float, enviar: int):
    conta_origem = buscarContaPorNumero(numero)
    conta_destino = buscarContaPorNumero(enviar)
    
    if conta_origem and conta_destino:
        if not conta_origem['ativo'] or not conta_destino['ativo']:
            print('Uma das contas não está ativa!')
            return
        if conta_origem['saldo'] >= valor:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            print(f'O valor de R$ {valor}, foi transferido para {conta_destino["nome"]}')
        else:
            print('Saldo insuficiente!')

# Menu
print('-'*30)
print('--- BEM VINDO AO MENU ---')
print('-'*30)
print('--- OPÇÕES ---')
print('1º - Listar contas')
print('2º - Criar conta')
print('3º - Buscar conta')
print('4º - Deletar conta')
print('5º - Editar conta')
print('6º - Ativar conta')
print('7º - Desativar conta')
print('8º - Depositar')
print('9º - Sacar')
print('10º - Transferência')
print('0º - Sair')

while True:
    codigo = int(input('Digite opção\n -> '))
    if codigo == 1:
        listar()
    elif codigo == 2:
        nome = input('Digite o nome para a nova conta\n -> ')
        addConta(nome)
    elif codigo == 3:
        numero = int(input('Digite o número da conta\n -> '))
        buscarContaPorNumero(numero)
    elif codigo == 4:
        numero = int(input('Digite o número da conta a deletar\n -> '))
        deletar(numero)
    elif codigo == 5:
        numero = int(input('Digite o número da conta a editar\n -> '))
        nome = input('Digite o novo nome\n -> ')
        editar(numero, nome)
    elif codigo == 6:
        numero = int(input('Digite o número da conta a ativar\n -> '))
        ativa(numero)
    elif codigo == 7:
        numero = int(input('Digite o número da conta a desativar\n -> '))
        desativar(numero)
    elif codigo == 8:
        numero = int(input('Digite o número da conta para depósito\n -> '))
        valor = float(input('Digite o valor para depositar\n -> '))
        depositar(numero, valor)
    elif codigo == 9:
        numero = int(input('Digite o número da conta para saque\n -> '))
        valor = float(input('Digite o valor para sacar\n -> '))
        sacar(numero, valor)
    elif codigo == 10:
        numero = int(input('Digite o número da conta de origem\n -> '))
        valor = float(input('Digite o valor para transferir\n -> '))
        numero2 = int(input('Digite o número da conta de destino\n -> '))
        transferencia(numero, valor, numero2)
    elif codigo == 0:
        print('Menu fechado!')
        break
        
    else:
        print('Opção inválida!')
