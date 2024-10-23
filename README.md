# Sistema Bancário

Este projeto é um sistema bancário simples implementado em Python, seguindo uma abordagem orientada a objetos. O sistema permite que os usuários criem contas, façam depósitos, saques e visualizem extratos bancários. Ele simula operações bancárias básicas, incluindo o rastreamento de transações e a gestão de contas, inspirado em um diagrama UML.

## Funcionalidades

- **Gerenciamento de Usuários**: 
  - Criar novos usuários com informações pessoais como nome, CPF, data de nascimento e endereço.
  
- **Gerenciamento de Contas**: 
  - Criar uma nova conta para um usuário existente.
  - Listar todas as contas existentes com seus detalhes.
  
- **Transações**: 
  - Realizar depósitos e saques em uma conta.
  - Limitar o número de saques por dia.
  - Definir limites de saque nas contas.
  - Histórico de transações com data e hora para cada conta.
  
- **Saldo e Extrato**: 
  - Exibir o saldo da conta e o histórico de transações em um formato fácil de ler.

## Diagrama de Classes

O sistema foi projetado com base em um diagrama de classes UML com os seguintes componentes principais:

- **Cliente**: Representa o usuário que possui contas.
- **Conta**: Representa uma conta bancária. Suporta operações básicas como depósito e saque.
- **Transacao**: Classe abstrata para representar transações bancárias, estendida por `Deposito` e `Saque`.
- **Historico**: Mantém um registro de todas as transações realizadas em uma conta.

## Começando

### Pré-requisitos

- Python 3.x é necessário para rodar este sistema.

### Como Usar

1. **Criar um novo usuário:**
   - Use a opção `[nu]` no menu para criar um novo usuário. Você será solicitado a inserir detalhes como CPF, nome, data de nascimento e endereço.

2. **Criar uma nova conta:**
   - Use a opção `[nc]` para criar uma nova conta para um usuário existente, fornecendo o CPF do usuário.

3. **Depositar dinheiro:**
   - Selecione a opção `[d]` para depositar dinheiro na conta de um usuário, fornecendo o CPF e o valor do depósito.

4. **Sacar dinheiro:**
   - Selecione a opção `[s]` para sacar dinheiro de uma conta, fornecendo o CPF e o valor do saque. Nota: existem limites para saques.

5. **Visualizar extrato da conta:**
   - Selecione a opção `[e]` para ver o histórico de transações e o saldo atual de uma conta, fornecendo o CPF.

6. **Listar todas as contas:**
   - Selecione a opção `[lc]` para visualizar todas as contas existentes.

7. **Sair do sistema:**
   - Selecione a opção `[q]` para sair do sistema.

## Melhorias Futuras

- Adicionar persistência (por exemplo, arquivos ou banco de dados) para armazenar os dados de usuários, contas e transações.
- Melhorar a validação de erros e entradas do usuário.
- Adicionar novos tipos de contas bancárias, como contas poupança ou contas de crédito.
