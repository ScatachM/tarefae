# Tarefaê

**Organize suas tarefas. Simplifique sua rotina.**

Aplicação web para gerenciamento de tarefas pessoais, acadêmicas e profissionais. O Tarefaê permite cadastrar, visualizar, editar, excluir e organizar atividades, acompanhar prazos e identificar tarefas atrasadas.

![Version](https://img.shields.io/badge/version-0.2.0-blue)
![Status](https://img.shields.io/badge/status-MVP%20implementado-success)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Tests](https://img.shields.io/badge/tests-10%20passing-brightgreen)
![License](https://img.shields.io/badge/license-not%20defined-lightgrey)

---

## Sobre o projeto

O Tarefaê é uma aplicação web desenvolvida para facilitar a organização de atividades pessoais, acadêmicas e profissionais.

A proposta surgiu da necessidade de centralizar tarefas, acompanhar prazos e organizar prioridades em um ambiente simples e intuitivo.

A aplicação permite que o usuário registre suas atividades, defina prioridades e datas de vencimento, acompanhe o status de cada tarefa e visualize quais atividades estão atrasadas.

O projeto foi desenvolvido individualmente como atividade prática de Engenharia de Software, aplicando conceitos de levantamento de requisitos, modelagem de dados, desenvolvimento incremental, testes automatizados e gerenciamento de projetos com Git e GitHub.

## Objetivos

- Facilitar a organização de atividades cotidianas.
- Centralizar informações sobre tarefas e prazos.
- Permitir o acompanhamento do progresso das atividades.
- Aplicar boas práticas de desenvolvimento de software.
- Exercitar o fluxo de trabalho com Git Flow, Issues e Pull Requests.

## Funcionalidades

### Implementadas

- [x] Cadastro de tarefas.
- [x] Listagem de tarefas.
- [x] Edição de tarefas.
- [x] Exclusão de tarefas.
- [x] Definição de prioridades: baixa, média e alta.
- [x] Definição de datas de vencimento.
- [x] Alteração do status: pendente ou concluída.
- [x] Filtros por status e prioridade.
- [x] Identificação visual de tarefas atrasadas.
- [x] Interface responsiva.
- [x] Persistência de dados com SQLite.
- [x] Testes automatizados com pytest.

### Planejadas para evoluções futuras

- [ ] Cadastro e autenticação de usuários.
- [ ] Organização de tarefas por categorias.
- [ ] Painel de estatísticas e produtividade.
- [ ] Notificações de vencimento.

## Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3 | Linguagem de programação |
| Flask | Framework para desenvolvimento web |
| SQLite | Banco de dados relacional |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e responsividade |
| Pytest | Testes automatizados |
| Git | Controle de versão |
| GitHub | Hospedagem e gerenciamento do projeto |

## Estrutura do projeto

```text
tarefae/
│
├── docs/
│   ├── project-charter.md
│   ├── requisitos.md
│   ├── casos-de-uso.md
│   ├── user-stories.md
│   └── modelo-dados.md
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── tarefas.py
│   ├── templates/
│   │   ├── index.html
│   │   └── editar.html
│   └── static/
│       └── css/
│           └── style.css
│
├── tests/
│   ├── conftest.py
│   └── test_tarefas.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

O banco de dados SQLite é criado localmente na pasta `instance/` durante a execução da aplicação. Arquivos temporários, ambientes virtuais e bancos de dados locais são ignorados pelo Git.

## Documentação

Os documentos de engenharia estão disponíveis na pasta `docs/`.

| Documento | Descrição |
|---|---|
| [Project Charter](docs/project-charter.md) | Termo de abertura, objetivos, escopo e stakeholders. |
| [Requisitos](docs/requisitos.md) | Requisitos funcionais, não funcionais e regras de negócio. |
| [Casos de Uso](docs/casos-de-uso.md) | Especificação das interações entre usuário e sistema. |
| [Histórias de Usuário](docs/user-stories.md) | Histórias de usuário e critérios de aceite. |
| [Modelo de Dados](docs/modelo-dados.md) | Estrutura de dados e modelagem do banco. |

## Configuração do ambiente

### Pré-requisitos

- Python 3 instalado.
- Git instalado.
- Navegador web atualizado.

### 1. Clonar o repositório

```bash
git clone https://github.com/ScatachM/tarefae.git
```

### 2. Acessar a pasta do projeto

```bash
cd tarefae
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows (Git Bash):

```bash
source venv/Scripts/activate
```

No Linux ou macOS:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Executar a aplicação

```bash
python -m flask --app src.app run --debug
```

A aplicação estará disponível em:

http://127.0.0.1:5000

## Testes automatizados

O projeto utiliza o framework pytest para verificar o funcionamento das principais funcionalidades da aplicação.

Os testes utilizam um banco de dados temporário, mantendo os dados reais da aplicação isolados.

### Executar os testes

Com o ambiente virtual ativado e as dependências instaladas, execute:

```bash
python -m pytest -v
```

### Cenários testados

- Carregamento da página inicial.
- Cadastro de tarefas.
- Validação de título obrigatório.
- Edição de tarefas.
- Exclusão de tarefas.
- Filtragem por status.
- Filtragem por prioridade

