# 💰 Sistema Bancário em Python

Este projeto é um Sistema Bancário, desenvolvido no âmbito do Bootcamp de Engenharia de Dados com Python da DIO - NTT DATA, com o objetivo de implementar três operações bancárias essenciais: Depósito, Saque e Extrato. O sistema foi projetado com foco na simplicidade, permitindo que o usuário realize operações básicas em uma conta bancária. Além de consolidar o conhecimento em Python, o projeto "Criando um Sistema Bancário com Python" proporciona uma experiência prática no desenvolvimento de software financeiro. Os participantes são desafiados a construir um sistema completo, abordando desde a criação de contas e execução de transações até aspectos de segurança, oferecendo uma oportunidade de aprimorar as habilidades de programação em Python e obter uma compreensão mais profunda de conceitos financeiros e segurança.



## 🚀 Funcionalidades

- **Depósito**: Permite realizar depósitos de valores positivos na conta bancária. 💵
- **Saque**: Limita o número de saques a **3 por dia**, com um valor máximo de **R$ 500,00** por saque. ❌💸
- **Extrato**: Exibe o histórico completo de depósitos e saques, além do saldo atual da conta. 📄💲

## ⚙️ Regras de Negócio

1. O sistema só permite **valores positivos** nos depósitos.
2. O **limite diário** de saques é de **3 saques**.
3. O valor máximo por saque é de **R$ 500,00**.
4. Se o usuário tentar sacar mais do que o saldo disponível, o sistema exibirá uma mensagem de **saldo insuficiente**.
5. O **extrato** exibe todas as movimentações e o saldo final.

## 🛠️ Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
  **Python**: Linguagem principal utilizada para o desenvolvimento do sistema.

- ![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)  
  **VS Code**: Editor de código utilizado no desenvolvimento do projeto.

## 📊 Exemplo de Execução

```bash
Bem-vindo ao Banco!
[1] Depositar
[2] Sacar
[3] Extrato
[5] Sair
