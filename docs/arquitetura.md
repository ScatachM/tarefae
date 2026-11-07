# Arquitetura do Sistema — Tarefaê



**Versão:** 1.0.0



**Data:** 07/11/2026



**Status:** Em desenvolvimento



## 1. Introdução



Este documento apresenta a arquitetura técnica da aplicação Tarefaê, descrevendo sua organização interna, os componentes principais, suas responsabilidades e o fluxo de comunicação entre as camadas do sistema.



O Tarefaê utiliza Python e Flask no desenvolvimento da aplicação web, SQLite para persistência dos dados e HTML5 e CSS3 na construção da interface.



## 2. Visão geral da arquitetura



A aplicação utiliza uma arquitetura modular, organizada em componentes responsáveis pela inicialização do sistema, processamento das requisições, acesso aos dados e apresentação das informações.



Os principais componentes são:



- Aplicação Flask: responsável pela criação e configuração do sistema.

- Rotas: responsáveis pelo processamento das requisições e pelas operações relacionadas às tarefas.

- Banco de dados: responsável pela conexão e persistência dos dados.

- Interface: responsável pela apresentação das informações ao usuário.



## 3. Organização dos diretórios



```text

tarefae/

├── docs/

├── instance/

│   └── tarefae.db

├── src/

│   ├── routes/

│   │   ├── __init__.py

│   │   └── tarefas.py

│   ├── static/

│   │   └── css/

│   │       └── style.css

│   ├── templates/

│   │   ├── editar.html

│   │   └── index.html

│   ├── __init__.py

│   ├── app.py

│   └── database.py

└── tests/

```



## 4. Componentes e responsabilidades



### 4.1 Aplicação Flask — app.py



Responsável pela inicialização e configuração da aplicação.



A função `create_app()` utiliza o padrão Application Factory para criar a instância Flask, configurar o caminho do banco de dados, inicializar a estrutura do banco e registrar o Blueprint de tarefas.



### 4.2 Persistência — database.py



Responsável pelo gerenciamento do acesso ao banco de dados SQLite.



Suas principais funções são:



- Definir o caminho do banco de dados.

- Criar conexões com SQLite.

- Configurar o retorno dos registros como objetos acessíveis por coluna.

- Inicializar a tabela de tarefas.

- Definir restrições para os campos da tabela.



### 4.3 Rotas — routes/tarefas.py



Responsável pelo processamento das requisições relacionadas às tarefas.



O módulo utiliza o Blueprint `tarefas_bp` e implementa:



- Cadastro de tarefas.

- Listagem de tarefas.

- Edição de tarefas.

- Exclusão de tarefas.

- Filtragem por status e prioridade.

- Validação dos dados recebidos.

- Identificação de tarefas atrasadas.



### 4.4 Interface — templates e static



Os templates HTML são responsáveis pela apresentação das páginas da aplicação:



- `index.html`: listagem e cadastro de tarefas.

- `editar.html`: edição de tarefas.



O arquivo `style.css` define os estilos visuais da aplicação.



## 5. Modelo de dados



O banco de dados SQLite utiliza a tabela `tarefas`, composta pelos seguintes campos:



| Campo | Tipo | Descrição |

|---|---|---|

| id | INTEGER | Identificador único da tarefa. |

| titulo | TEXT | Título obrigatório. |

| descricao | TEXT | Descrição opcional. |

| prioridade | TEXT | Prioridade baixa, média ou alta. |

| status | TEXT | Situação pendente ou concluída. |

| data_criacao | TEXT | Data de criação gerada pelo banco. |

| data_vencimento | TEXT | Data de vencimento opcional. |



O identificador é definido como chave primária e possui incremento automático.



## 6. Fluxo de funcionamento



1. O usuário acessa a aplicação pelo navegador.

2. O navegador envia uma requisição HTTP ao servidor Flask.

3. O Blueprint direciona a requisição para a rota correspondente.

4. A rota processa os dados e realiza as validações necessárias.

5. Quando necessário, a rota utiliza `get_db_connection()` para acessar o SQLite.

6. O resultado é enviado ao template HTML correspondente.

7. O Flask retorna a resposta ao navegador.



Nas operações de cadastro, edição e exclusão, o sistema realiza as alterações no banco de dados e redireciona o usuário para a página inicial.



## 7. Tecnologias utilizadas



- Python 3: linguagem de programação.

- Flask: framework web.

- SQLite: banco de dados relacional.

- HTML5: estrutura das páginas.

- CSS3: apresentação visual.

- Pytest: testes automatizados.

- pytest-cov: medição da cobertura dos testes.



## 8. Testes e qualidade



O projeto utiliza Pytest para validar as principais funcionalidades da aplicação.



A execução mais recente registrou:



- 10 testes automatizados aprovados.

- Cobertura de código de 90,32%.

- Meta mínima de cobertura configurada em 80%.

- Integração contínua configurada com GitHub Actions.



## 9. Considerações finais



A arquitetura modular do Tarefaê busca organizar as responsabilidades da aplicação e facilitar sua manutenção e evolução.



A separação entre inicialização, rotas, persistência e apresentação permite que novas funcionalidades sejam incorporadas sem concentrar toda a lógica em um único módulo.



Este documento deverá ser atualizado sempre que alterações arquiteturais relevantes forem realizadas.

