\# Modelo de Dados — Tarefaê



\*\*Versão:\*\* 1.0.0  

\*\*Data:\*\* 06/11/2026  

\*\*Status:\*\* Em especificação



\## 1. Introdução



Este documento apresenta a modelagem de dados da aplicação Tarefaê, definindo a estrutura de armazenamento das informações utilizadas pelo sistema.



A modelagem foi elaborada com base nos requisitos funcionais, regras de negócio e casos de uso previamente especificados.



O banco de dados escolhido é o SQLite, por sua simplicidade, portabilidade e adequação ao escopo da primeira versão da aplicação.



\## 2. Modelo conceitual



O sistema possui inicialmente uma única entidade principal: Tarefa.



A entidade representa as atividades cadastradas pelo usuário e armazena informações necessárias para seu gerenciamento e acompanhamento.



\### 2.1. Entidade Tarefa



Cada registro representa uma tarefa independente.



\*\*Atributos:\*\*



\- id: identificador único da tarefa.

\- titulo: nome ou descrição resumida da atividade.

\- descricao: informações complementares sobre a tarefa.

\- prioridade: nível de importância da atividade.

\- status: situação atual da tarefa.

\- data\_criacao: data e horário em que a tarefa foi cadastrada.

\- data\_vencimento: prazo definido para conclusão da tarefa.



\## 3. Dicionário de dados



| Campo | Tipo SQLite | Obrigatório | Descrição |

|---|---|---|---|

| id | INTEGER | Sim | Identificador único, chave primária. |

| titulo | TEXT | Sim | Título da tarefa. |

| descricao | TEXT | Não | Descrição complementar. |

| prioridade | TEXT | Sim | Prioridade da tarefa. |

| status | TEXT | Sim | Situação da tarefa. |

| data\_criacao | TEXT | Sim | Data e horário de cadastro. |

| data\_vencimento | TEXT | Não | Data limite para conclusão. |



\## 4. Restrições e regras de integridade



A entidade Tarefa deverá respeitar as seguintes restrições:



\- O campo id será a chave primária e terá incremento automático.

\- O título deverá ser obrigatório e não poderá conter apenas espaços.

\- A descrição será opcional.

\- A prioridade deverá aceitar somente os valores baixa, media ou alta.

\- A prioridade padrão será media.

\- O status deverá aceitar somente os valores pendente ou concluida.

\- O status inicial será pendente.

\- A data de criação será preenchida automaticamente.

\- A data de vencimento será opcional.

\- As datas serão armazenadas em formato ISO 8601.



\## 5. Modelo físico



A tabela principal será denominada `tarefa`.



\### 5.1. Script de criação



```sql

CREATE TABLE IF NOT EXISTS tarefa (

&#x20;   id INTEGER PRIMARY KEY AUTOINCREMENT,

&#x20;   titulo TEXT NOT NULL

&#x20;       CHECK (length(trim(titulo)) > 0),

&#x20;   descricao TEXT,

&#x20;   prioridade TEXT NOT NULL DEFAULT 'media'

&#x20;       CHECK (prioridade IN ('baixa', 'media', 'alta')),

&#x20;   status TEXT NOT NULL DEFAULT 'pendente'

&#x20;       CHECK (status IN ('pendente', 'concluida')),

&#x20;   data\_criacao TEXT NOT NULL DEFAULT CURRENT\_TIMESTAMP,

&#x20;   data\_vencimento TEXT

);

```



\## 6. Relacionamento entre entidades



Na primeira versão do Tarefaê, existe apenas a entidade Tarefa.



Portanto, não existem relacionamentos entre tabelas nesta etapa do projeto.



Caso sejam implementadas funcionalidades como autenticação ou compartilhamento de tarefas em versões futuras, novas entidades e relacionamentos poderão ser incorporados.



\## 7. Requisitos relacionados



A modelagem atende aos seguintes requisitos:



| Requisito | Aplicação no modelo |

|---|---|

| RF01 | Armazenamento dos dados de cadastro. |

| RF02 | Consulta das tarefas armazenadas. |

| RF03 | Consulta dos detalhes de uma tarefa. |

| RF04 | Atualização dos atributos da tarefa. |

| RF05 | Exclusão de registros. |

| RF06 | Armazenamento da prioridade. |

| RF07 | Armazenamento da data de vencimento. |

| RF08 | Armazenamento e atualização do status. |

| RF09 | Consulta por status. |

| RF10 | Consulta por prioridade. |

| RF11 | Identificação de tarefas atrasadas por meio do status e da data de vencimento. |

| RNF03 | Persistência das informações utilizando SQLite. |

| RNF06 | Separação da estrutura de dados da lógica da aplicação. |



\## 8. Considerações finais



O modelo de dados foi elaborado para atender às necessidades da primeira versão do Tarefaê, priorizando simplicidade, integridade e facilidade de manutenção.



A estrutura poderá ser ampliada em versões futuras, conforme a evolução dos requisitos e das funcionalidades da aplicação.

