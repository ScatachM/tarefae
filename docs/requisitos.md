\# Requisitos do Sistema — Tarefaê



\*\*Versão:\*\* 1.0.0  

\*\*Data:\*\* 06/11/2026  

\*\*Status:\*\* Em especificação



\## 1. Introdução



Este documento apresenta os requisitos funcionais, não funcionais e as regras de negócio da aplicação Tarefaê.



O objetivo é estabelecer as funcionalidades e características necessárias para o desenvolvimento do sistema, servindo como referência para implementação, testes e validação.



\## 2. Requisitos Funcionais (RF)



| ID | Descrição |

|---|---|

| RF01 | O sistema deve permitir cadastrar uma nova tarefa, informando título e, opcionalmente, descrição. |

| RF02 | O sistema deve permitir visualizar a lista de tarefas cadastradas. |

| RF03 | O sistema deve permitir visualizar os detalhes de uma tarefa específica. |

| RF04 | O sistema deve permitir editar as informações de uma tarefa existente. |

| RF05 | O sistema deve permitir excluir uma tarefa cadastrada. |

| RF06 | O sistema deve permitir definir a prioridade de uma tarefa entre baixa, média e alta. |

| RF07 | O sistema deve permitir definir uma data de vencimento para cada tarefa. |

| RF08 | O sistema deve permitir alterar o status de uma tarefa entre pendente e concluída. |

| RF09 | O sistema deve permitir filtrar as tarefas pelo status. |

| RF10 | O sistema deve permitir filtrar as tarefas pela prioridade. |

| RF11 | O sistema deve identificar visualmente as tarefas atrasadas. |



\## 3. Requisitos Não Funcionais (RNF)



| ID | Categoria | Descrição |

|---|---|---|

| RNF01 | Usabilidade | A interface deve ser intuitiva, facilitando a utilização por pessoas sem conhecimentos técnicos avançados. |

| RNF02 | Desempenho | As operações comuns devem apresentar resposta em até 2 segundos no ambiente local, considerando o volume de dados previsto para o MVP. |

| RNF03 | Persistência | Os dados cadastrados devem permanecer armazenados após o encerramento da aplicação. |

| RNF04 | Portabilidade | A aplicação deve funcionar nos principais navegadores modernos. |

| RNF05 | Responsividade | A interface deve adaptar-se a diferentes tamanhos de tela. |

| RNF06 | Manutenibilidade | O código-fonte deve ser organizado em módulos, separando as responsabilidades da aplicação. |

| RNF07 | Confiabilidade | O sistema deve validar os dados recebidos antes de executar operações de cadastro e edição. |

| RNF08 | Testabilidade | As principais funcionalidades devem possuir testes automatizados utilizando Pytest. |

| RNF09 | Segurança | O sistema deve validar e tratar as entradas recebidas, utilizar consultas parametrizadas no banco de dados e evitar vulnerabilidades comuns. |



\## 4. Regras de Negócio (RN)



| ID | Descrição |

|---|---|

| RN01 | Toda tarefa deve possuir um título obrigatório. |

| RN02 | A descrição da tarefa é opcional. |

| RN03 | Toda tarefa deve possuir uma prioridade. |

| RN04 | A prioridade padrão de uma nova tarefa deve ser média. |

| RN05 | Toda tarefa deve ser cadastrada inicialmente com status pendente. |

| RN06 | A data de vencimento é opcional. |

| RN07 | Uma tarefa concluída não deve ser considerada pendente. |

| RN08 | Uma tarefa será considerada atrasada quando sua data de vencimento for anterior à data atual e seu status permanecer pendente. |

| RN09 | Uma tarefa excluída não deverá permanecer disponível na listagem do sistema. |



\## 5. Rastreabilidade dos Requisitos



Os requisitos serão relacionados aos casos de uso, às histórias de usuário e às Issues do GitHub.



| Requisito | Caso de uso | História de usuário |

|---|---|---|

| RF01 | UC01 | US01 |

| RF02 | UC02 | US02 |

| RF03 | UC02 | US02 |

| RF04 | UC03 | US03 |

| RF05 | UC04 | US04 |

| RF06 | UC01 / UC03 | US01 / US03 |

| RF07 | UC01 / UC03 | US01 / US03 |

| RF08 | UC05 | US05 |

| RF09 | UC06 | US06 |

| RF10 | UC06 | US06 |

| RF11 | UC02 | US02 |



\## 6. Tecnologias relacionadas



\- Python 3: desenvolvimento da lógica da aplicação.

\- Flask: gerenciamento das rotas e requisições web.

\- SQLite: persistência dos dados.

\- HTML5 e CSS3: estrutura e apresentação da interface.

\- JavaScript: interatividade.

\- Pytest: testes automatizados.



\## 7. Considerações finais



Os requisitos apresentados representam o escopo funcional e técnico da primeira versão do Tarefaê.



Alterações ou inclusões de requisitos deverão ser documentadas e relacionadas ao backlog do projeto, mantendo a rastreabilidade entre especificação, implementação e testes.

