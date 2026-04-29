# Version_3B_Criar_Integracao_Continua
CI na Prática
PASSO A PASSO: CRIAR UMA ESTEIRA (CI) NO GITHUB


PASSO 1 — Criar repositório
Acesse o GitHub
Clique em New repository
Dê um nome (ex: agenda-python)
Clique em Create repository

PASSO 2 — Subir seu código
Você pode:
Fazer upload direto (Upload files)
Ou usar Git

PASSO 3 — Criar pasta da esteira
No repositório:
Clique em Add file → Create new file
Crie o caminho:
.github/workflows/main.yml
👉 Isso ativa a esteira

PASSO 4 — Criar o arquivo da esteira
Cole este código simples (nível iniciante):
name: CI Simples

# Quando executar
on:
 push:
   branches: [ "main" ]

jobs:
 build:
   runs-on: ubuntu-latest

   steps:
     # Baixa o código
     - name: Baixar código
       uses: actions/checkout@v3

     # Instala Python
     - name: Instalar Python
       uses: actions/setup-python@v4
       with:
         python-version: '3.10'

     # Executa o programa
     - name: Rodar código
       run: python seu_arquivo.py

PASSO 5 — Salvar (commit)
Clique em:
 👉 Commit changes

PASSO 6 — Ver a esteira funcionando
Vá na aba Actions
Você verá a execução automática

