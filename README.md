\# Tarefaê



\*\*Organize suas tarefas. Simplifique sua rotina.\*\*



Aplicação web para gerenciamento de tarefas pessoais, permitindo cadastrar, organizar, priorizar e acompanhar atividades cotidianas.



!\[Version](https://img.shields.io/badge/version-0.1.0-blue)

!\[Status](https://img.shields.io/badge/status-in%20development-yellow)

!\[Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

!\[Flask](https://img.shields.io/badge/Flask-framework-black?logo=flask)

!\[SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)

!\[License](https://img.shields.io/badge/license-not%20defined-lightgrey)



\---



\## Sobre o projeto



O Tarefaê é uma aplicação web desenvolvida para facilitar a organização de atividades pessoais, acadêmicas e profissionais.



A proposta surgiu da necessidade de centralizar tarefas, acompanhar prazos e organizar prioridades em um ambiente simples e intuitivo.



Por meio da aplicação, o usuário poderá cadastrar atividades, acompanhar seu andamento, definir datas de vencimento e identificar tarefas pendentes ou concluídas.



O projeto está sendo desenvolvido como parte de uma atividade acadêmica de Engenharia de Software, aplicando conceitos de especificação de requisitos, modelagem de dados, versionamento e desenvolvimento incremental.



\## Objetivos



\- Facilitar a organização de atividades cotidianas.

\- Centralizar informações sobre tarefas e prazos.

\- Permitir o acompanhamento do progresso das atividades.

\- Aplicar boas práticas de desenvolvimento de software.



\## Funcionalidades



\### Planejadas para o MVP



\- \[ ] Cadastro de tarefas.

\- \[ ] Listagem de tarefas.

\- \[ ] Visualização dos detalhes de uma tarefa.

\- \[ ] Edição de tarefas.

\- \[ ] Exclusão de tarefas.

\- \[ ] Definição de prioridades.

\- \[ ] Definição de datas de vencimento.

\- \[ ] Alteração do status das tarefas.

\- \[ ] Filtros por status e prioridade.

\- \[ ] Identificação visual de tarefas atrasadas.



\### Implementação



As funcionalidades serão marcadas como concluídas conforme forem implementadas, testadas e integradas à branch `develop`.



\## Tecnologias utilizadas



| Tecnologia | Aplicação |

|---|---|

| Python 3 | Linguagem de programação principal. |

| Flask | Framework para desenvolvimento web. |

| SQLite | Banco de dados relacional. |

| HTML5 | Estrutura das páginas. |

| CSS3 | Estilização e responsividade. |

| JavaScript | Interatividade da interface. |

| Pytest | Testes automatizados. |

| Git | Controle de versão. |

| GitHub | Hospedagem e gerenciamento do projeto. |



\## Estrutura do projeto



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

│   ├── app.py

│   ├── database.py

│   ├── models/

│   ├── routes/

│   ├── templates/

│   └── static/

│

├── tests/

│

├── .gitignore

├── requirements.txt

└── README.md

```



\## Documentação



Os documentos de engenharia do projeto estão disponíveis na pasta `docs/`.



| Documento | Descrição |

|---|---|

| \[Project Charter](docs/project-charter.md) | Termo de abertura, objetivos, escopo e stakeholders. |

| \[Requisitos](docs/requisitos.md) | Requisitos funcionais, não funcionais e regras de negócio. |

| \[Casos de Uso](docs/casos-de-uso.md) | Especificação das interações entre usuário e sistema. |

| \[Histórias de Usuário](docs/user-stories.md) | Histórias de usuário e critérios de aceite. |

| \[Modelo de Dados](docs/modelo-dados.md) | Estrutura da entidade Tarefa e modelo físico do banco de dados. |



\## Configuração do ambiente



\### Pré-requisitos



Antes de executar o projeto, é necessário possuir:



\- Python 3 instalado.

\- Git instalado.

\- Um editor de código, como Visual Studio Code.

\- Um navegador web atualizado.



\### 1. Clonar o repositório



```bash

git clone https://github.com/ScatachM/tarefae.git

```



\### 2. Acessar a pasta do projeto



```bash

cd tarefae

```



\### 3. Criar um ambiente virtual



```bash

python -m venv venv

```



\### 4. Ativar o ambiente virtual



No Windows:



```bash

venv\\Scripts\\activate

```



No Linux ou macOS:



```bash

source venv/bin/activate

```



\### 5. Instalar as dependências



```bash

pip install -r requirements.txt

```



\### 6. Executar a aplicação



Após a implementação da aplicação Flask:



```bash

python -m flask --app src.app run --debug

```



A aplicação estará disponível localmente em:



```text

http://127.0.0.1:5000

```



\*\*Observação:\*\* os comandos de execução representam o procedimento previsto para a versão funcional. A aplicação e suas dependências ainda estão em desenvolvimento.



\## Executar os testes



Após a implementação dos testes automatizados, execute:



```bash

pytest

```



\## Fluxo de desenvolvimento — Git Flow



O projeto utiliza uma versão simplificada do Git Flow para organizar o desenvolvimento.



| Branch | Finalidade |

|---|---|

| `main` | Armazenar versões estáveis do projeto. |

| `develop` | Integrar as funcionalidades em desenvolvimento. |

| `feature/\*` | Implementar funcionalidades ou tarefas específicas. |



\### Fluxo de trabalho



```text

main

&#x20; |

&#x20; |

develop

&#x20; |

&#x20; |---- feature/issue-01

&#x20; |

&#x20; |---- feature/issue-02

&#x20; |

&#x20; |---- feature/issue-03

&#x20; |

&#x20; |---- feature/issue-XX

&#x20; |

&#x20; v

Pull Request → develop

```



As branches temáticas devem ser criadas a partir de `develop` e integradas por Pull Requests após revisão.



Não são realizados commits diretamente na branch `main`.



\### Padrão de commits



O projeto utiliza Conventional Commits.



Exemplos:



```text

feat(tasks): implement task registration

fix(tasks): correct task validation

docs(requirements): update system requirements

test(tasks): add task creation tests

refactor(database): organize database operations

```



\### Versionamento semântico



O versionamento segue o padrão SemVer:



`MAJOR.MINOR.PATCH`



Exemplo: `v1.0.0`.



\- MAJOR: mudanças incompatíveis.

\- MINOR: novas funcionalidades compatíveis.

\- PATCH: correções de defeitos.



\## Gestão do projeto



O acompanhamento das atividades é realizado por meio do GitHub Issues.



Cada Issue representa uma unidade de trabalho, contendo descrição, requisitos relacionados e critérios de aceite.



Os Pull Requests são vinculados às respectivas Issues para garantir rastreabilidade entre planejamento, implementação e entrega.



\## Licença



A licença do projeto ainda não foi definida.



\## Autoria



Projeto acadêmico desenvolvido individualmente como atividade prática de Engenharia de Software.



\*\*Tarefaê — Organize suas tarefas. Simplifique sua rotina.\*\*

## Testes automatizados

O projeto utiliza o framework pytest para verificar o funcionamento das principais funcionalidades da aplicação.

### Executar os testes

Com o ambiente virtual ativado e as dependências instaladas, execute:

```bash
python -m pytest -v

