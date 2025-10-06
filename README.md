🏦 Sistema Bancário em Python
📋 Descrição

Este projeto implementa um sistema bancário simples desenvolvido em Python, com foco em aplicar conceitos de lógica de programação, estruturas condicionais e laços de repetição.

O sistema permite ao usuário realizar operações básicas bancárias, como:

Depósito

Saque

Consulta de extrato

O código foi desenvolvido de forma didática para demonstrar como um sistema pode gerenciar operações financeiras de maneira simples e eficiente.

🚀 Funcionalidades

Depósito:
Permite adicionar um valor positivo ao saldo da conta.

Saque:
O usuário pode sacar valores dentro do limite estabelecido (R$500 por saque).
Há também um limite diário de 3 saques.

Extrato:
Exibe todas as movimentações realizadas e o saldo atual da conta.

Controle de erros:
O sistema impede depósitos e saques com valores inválidos, além de avisar sobre saldo insuficiente ou limite excedido.

🧠 Lógica do Código

O código é baseado em programação estruturada, usando variáveis globais e um laço while para manter o sistema em execução até o usuário escolher sair.

Principais variáveis:

saldo: guarda o valor total da conta.

limite: define o valor máximo permitido por saque.

extrato: armazena o histórico de movimentações (depósitos e saques).

numero_saques: controla quantos saques foram feitos no dia.

LIMITE_SAQUES: define o número máximo de saques permitidos por sessão.

Estrutura principal (while True):

Exibe um menu com as opções disponíveis.

Lê a escolha do usuário.

Executa a operação correspondente (if, elif, else).

Exibe mensagens informativas sobre cada ação.

🧩 Fluxo de Execução

O usuário escolhe uma das opções do menu.

O sistema executa a função correspondente:

[1] → Depósito

[2] → Saque

[3] → Extrato

[4] → Sair

O laço continua até o usuário encerrar o programa.

======= MENU =======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
====================
Escolha uma opção: 1

Informe o valor do depósito: R$ 300
Depósito de R$ 300.00 realizado com sucesso!

======= MENU =======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
====================
Escolha uma opção: 3

======= EXTRATO =======
Depósito: +R$ 300.00

Saldo atual: R$ 300.00
========================

🧱 Tecnologias Utilizadas

Linguagem: Python 3

Paradigma: Programação Estruturada

🎯 Objetivo Educacional

Este projeto tem como finalidade praticar:

Lógica de programação

Manipulação de variáveis e strings

Estruturas condicionais (if/elif/else)

Laços de repetição (while)

Interação com o usuário via terminal

🧑‍💻 Autor

João Vitor Mendes
Projeto desenvolvido como exercício prático de Python, simulando operações bancárias reais em um ambiente controlado.
