# Python-Web-Api
Desenvolvimento web com python 


# Blog CLI

Este projeto contem uma interface de linha de comando (CLI) para gerenciar postagens em um blog utilizando Flask e MongoDB. 
Com esta CLI, você pode facilmente adicionar, atualizar, listar, obter e deletar postagens diretamente do terminal.

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>

2. Crie um ambiente virtual e ative-o:
`python -m venv .venv`
`source .venv/bin/activate`  
No Windows, use: `.venv\Scripts\activate`

3. Instale as dependencias
```pip install -r requirements.txt```

4. Configure o MongoDB e adicione as credenciais necessárias.

### Configuração do Flask

Antes de utilizar a CLI, é importante garantir que a variável de ambiente FLASK_APP esteja configurada. 
Você pode fazer isso definindo a variável no terminal:
```export FLASK_APP=app.py  # ou o nome do seu arquivo principal```

### Comandos Disponíveis

Para visualizar todos os comandos disponíveis, você pode usar:

`flask --help`

### Grupo de Comandos post

O comando post permite gerenciar as postagens do blog. Aqui estão os subcomandos disponíveis:
`flask post --help`

1. Listar Postagens

Para listar todas as postagens:
`flask post list`

2. Adicionar Nova Postagem

Para adicionar uma nova postagem:

`flask post new --title "Título da Postagem" --content "Conteúdo da postagem"`

3. Obter Postagem por Slug

Para obter uma postagem específica pelo seu slug:

`flask post get <slug>`


4. Atualizar Postagem

Para atualizar uma postagem existente:

`flask post update <slug> --content "Novo conteúdo" --published`

5. Deletar Postagem

Para deletar uma postagem pelo seu slug:

`flask post delete <slug>`

Exemplo:

`flask post delete meu-primeiro-post`

### Ajuda

Para obter ajuda sobre qualquer comando específico, você pode usar --help. 
Por exemplo, para o comando de deleção:

`flask post delete --help`


### Verificação de Padrões com Ruff

Este projeto utiliza o Ruff como ferramenta de linting para garantir a qualidade e a conformidade do código com as melhores práticas de desenvolvimento em Python.
O que é o Ruff?

Ruff é uma ferramenta rápida e eficiente de linting e formatação que ajuda a identificar problemas no código, como erros de estilo, bugs potenciais e muito mais.
#### Como o Ruff é Usado Neste Projeto

    Verificação Contínua: O código é verificado regularmente com o Ruff para assegurar que todos os padrões de codificação estão sendo seguidos.
    Feedback Imediato: Os desenvolvedores recebem feedback instantâneo sobre problemas no código, facilitando a manutenção e a colaboração.

#### Executando o Ruff

Para verificar o código do projeto, você pode usar o seguinte comando:


`ruff check <diretório ou arquivo>`

Por exemplo, para verificar a pasta blog:


`ruff check blog/`



[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

