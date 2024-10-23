# -*- coding: utf-8 -*-
"""sistema_bancário_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AxgYHe17JbOhQf4P8DCbiEV8Aif-4KNg
"""

import textwrap
from datetime import datetime

# Class definitions based on the UML diagram

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        conta.adicionar_transacao(transacao)

class Conta:
    LIMITE_SAQUES = 3

    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()
        self.limite = 500.0
        self.numero_saques = 0
        self.cliente.adicionar_conta(self)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            deposito = Deposito(valor)
            self.historico.adicionar_transacao(deposito)
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= Conta.LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            saque = Saque(valor)
            self.historico.adicionar_transacao(saque)
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        self.historico.mostrar_historico()
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite, limite_saques):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar_historico(self):
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        for transacao in self.transacoes:
            print(f"{transacao.tipo}:\t\tR$ {transacao.valor:.2f} ({transacao.data})")

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self.tipo = "Depósito"

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self.tipo = "Saque"

# Functionality

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = Cliente(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)

    print("=== Usuário criado com sucesso! ===")

def criar_conta(numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        nova_conta = ContaCorrente(numero_conta, usuario, limite=500, limite_saques=3)
        print("\n=== Conta criada com sucesso! ===")
        return nova_conta

    print("\n@@@ Usuário não encontrado! @@@")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta foi cadastrada. @@@")
        return

    for conta in contas:
        print("=" * 100)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero}")
        print(f"Titular:\t{conta.cliente.nome}")

def main():
    usuarios = []
    contas = []
    numero_conta = 0

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do titular: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                conta = usuario.contas[0]  # Assuming user has only one account for simplicity
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "s":
            cpf = input("Informe o CPF do titular: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                conta = usuario.contas[0]  # Assuming user has only one account for simplicity
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "e":
            cpf = input("Informe o CPF do titular: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario and usuario.contas:
                conta = usuario.contas[0]  # Assuming user has only one account for simplicity
                conta.exibir_extrato()
            else:
                print("\n@@@ Conta não encontrada! @@@")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta += 1
            conta = criar_conta(numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida! Tente novamente. @@@")

main()