<div align="center">

<h1>🏦 Sistema Bancário em Python</h1>

<h2>📋 Descrição</h2>

<p align="justify">
Este projeto implementa um <b>sistema bancário simples</b> desenvolvido em <b>Python</b>, com foco em aplicar conceitos de 
<b>lógica de programação</b>, <b>estruturas condicionais</b> e <b>laços de repetição</b>.<br><br>

O sistema permite ao usuário realizar operações básicas bancárias, como:
</p>

<ul align="left">
  <li>Depósito</li>
  <li>Saque</li>
  <li>Consulta de extrato</li>
</ul>

<p align="justify">
O código foi desenvolvido de forma didática para demonstrar como um sistema pode gerenciar operações financeiras de maneira simples e eficiente.
</p>

---

<h2>🚀 Funcionalidades</h2>

<ul align="left">
  <li><b>Depósito:</b> Permite adicionar um valor positivo ao saldo da conta.</li>
  <li><b>Saque:</b> O usuário pode sacar valores dentro do limite estabelecido (R$500 por saque). Há também um limite diário de 3 saques.</li>
  <li><b>Extrato:</b> Exibe todas as movimentações realizadas e o saldo atual da conta.</li>
  <li><b>Controle de erros:</b> O sistema impede depósitos e saques com valores inválidos, além de avisar sobre saldo insuficiente ou limite excedido.</li>
</ul>

---

<h2>🧠 Lógica do Código</h2>

<p align="justify">
O código é baseado em <b>programação estruturada</b>, usando variáveis globais e um laço <code>while</code> 
para manter o sistema em execução até o usuário escolher sair.
</p>

<h4>Principais variáveis:</h4>
<ul align="left">
  <li><b>saldo:</b> guarda o valor total da conta.</li>
  <li><b>limite:</b> define o valor máximo permitido por saque.</li>
  <li><b>extrato:</b> armazena o histórico de movimentações (depósitos e saques).</li>
  <li><b>numero_saques:</b> controla quantos saques foram feitos no dia.</li>
  <li><b>LIMITE_SAQUES:</b> define o número máximo de saques permitidos por sessão.</li>
</ul>

<p align="justify">
<b>Estrutura principal (<code>while True</code>):</b><br>
1. Exibe um menu com as opções disponíveis.<br>
2. Lê a escolha do usuário.<br>
3. Executa a operação correspondente (<code>if</code>, <code>elif</code>, <code>else</code>).<br>
4. Exibe mensagens informativas sobre cada ação.
</p>

---

<h2>🧩 Fluxo de Execução</h2>

<p align="justify">
O usuário escolhe uma das opções do menu e o sistema executa a função correspondente:
</p>

<pre align="left">
[1] → Depósito
[2] → Saque
[3] → Extrato
[4] → Sair
</pre>

<p align="justify">
O laço continua até o usuário encerrar o programa.
</p>

<pre align="left">
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
</pre>

---

<h2>🧱 Tecnologias Utilizadas</h2>

<ul align="left">
  <li><b>Linguagem:</b> Python 3</li>
  <li><b>Paradigma:</b> Programação Estruturada</li>
</ul>

---

<h2>🎯 Objetivo Educacional</h2>

<p align="justify">
Este projeto tem como finalidade praticar:
</p>

<ul align="left">
  <li>Lógica de programação</li>
  <li>Manipulação de variáveis e strings</li>
  <li>Estruturas condicionais (<code>if/elif/else</code>)</li>
  <li>Laços de repetição (<code>while</code>)</li>
  <li>Interação com o usuário via terminal</li>
</ul>

---

<h2>🧑‍💻 Autor</h2>

<p><b>João Vitor Mendes</b><br>
Projeto desenvolvido como exercício prático de Python, simulando operações bancárias reais em um ambiente controlado.
</p>

</div>
