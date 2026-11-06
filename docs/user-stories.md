\# Histórias de Usuário — Tarefaê



\*\*Versão:\*\* 1.0.0  

\*\*Data:\*\* 06/11/2026  

\*\*Status:\*\* Em especificação



\## 1. Introdução



Este documento apresenta as histórias de usuário da aplicação Tarefaê, descrevendo as necessidades dos usuários e os benefícios esperados com as funcionalidades do sistema.



As histórias foram elaboradas a partir dos requisitos funcionais e dos casos de uso definidos nos documentos anteriores.



Cada história possui critérios de aceite estruturados no padrão BDD (Behavior-Driven Development), utilizando a abordagem Gherkin: Dado, Quando e Então.



\## 2. Histórias de usuário



\### US01 — Cadastrar tarefas



\*\*História:\*\*



Como usuário, quero cadastrar tarefas com título, descrição, prioridade e data de vencimento para organizar minhas atividades e acompanhar seus prazos.



\*\*Requisitos relacionados:\*\* RF01, RF06, RF07.



\*\*Caso de uso relacionado:\*\* UC01.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Cadastrar uma tarefa com sucesso\*\*



\- Dado que o usuário esteja na tela de cadastro de tarefas;

\- Quando informar um título válido e confirmar o cadastro;

\- Então o sistema deve armazenar a tarefa e apresentá-la na listagem.



\*\*Cenário 2 — Impedir cadastro sem título\*\*



\- Dado que o usuário esteja preenchendo o formulário de cadastro;

\- Quando tentar cadastrar uma tarefa sem informar o título;

\- Então o sistema deve impedir o cadastro e apresentar uma mensagem de validação.



\*\*Cenário 3 — Cadastrar tarefa sem descrição e vencimento\*\*



\- Dado que o usuário esteja preenchendo o formulário;

\- Quando informar somente o título e confirmar o cadastro;

\- Então o sistema deve permitir o registro, mantendo a descrição e a data de vencimento vazias.



\*\*Cenário 4 — Utilizar valores padrão\*\*



\- Dado que o usuário esteja cadastrando uma nova tarefa sem selecionar prioridade;

\- Quando confirmar o cadastro;

\- Então o sistema deve atribuir prioridade média e status pendente.



\### US02 — Consultar tarefas



\*\*História:\*\*



Como usuário, quero visualizar minhas tarefas e seus detalhes para acompanhar minhas atividades e identificar aquelas que estão atrasadas.



\*\*Requisitos relacionados:\*\* RF02, RF03, RF11.



\*\*Caso de uso relacionado:\*\* UC02.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Visualizar tarefas cadastradas\*\*



\- Dado que existam tarefas armazenadas no sistema;

\- Quando o usuário acessar a página principal;

\- Então o sistema deve apresentar a lista de tarefas cadastradas.



\*\*Cenário 2 — Consultar detalhes de uma tarefa\*\*



\- Dado que existam tarefas cadastradas;

\- Quando o usuário selecionar uma tarefa;

\- Então o sistema deve apresentar seus detalhes, incluindo título, descrição, prioridade, status e datas.



\*\*Cenário 3 — Consultar lista vazia\*\*



\- Dado que não existam tarefas cadastradas;

\- Quando o usuário acessar a página principal;

\- Então o sistema deve apresentar uma mensagem informando que não existem tarefas cadastradas.



\*\*Cenário 4 — Identificar tarefas atrasadas\*\*



\- Dado que exista uma tarefa pendente com data de vencimento anterior à data atual;

\- Quando o usuário visualizar a lista de tarefas;

\- Então o sistema deve apresentar uma indicação visual de atraso.



\### US03 — Editar tarefas



\*\*História:\*\*



Como usuário, quero editar as informações de uma tarefa para manter meus registros atualizados conforme minhas necessidades.



\*\*Requisitos relacionados:\*\* RF04, RF06, RF07.



\*\*Caso de uso relacionado:\*\* UC03.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Editar uma tarefa com sucesso\*\*



\- Dado que exista uma tarefa cadastrada;

\- Quando o usuário alterar suas informações e confirmar a edição;

\- Então o sistema deve atualizar os dados no banco de dados e apresentar a versão atualizada.



\*\*Cenário 2 — Impedir edição sem título\*\*



\- Dado que o usuário esteja editando uma tarefa;

\- Quando remover o título e tentar salvar as alterações;

\- Então o sistema deve impedir a atualização e apresentar uma mensagem de validação.



\*\*Cenário 3 — Cancelar edição\*\*



\- Dado que o usuário esteja editando uma tarefa;

\- Quando cancelar a operação;

\- Então o sistema deve descartar as alterações não salvas e manter os dados originais.



\### US04 — Excluir tarefas



\*\*História:\*\*



Como usuário, quero excluir tarefas que não são mais necessárias para manter minha lista organizada.



\*\*Requisito relacionado:\*\* RF05.



\*\*Caso de uso relacionado:\*\* UC04.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Excluir uma tarefa\*\*



\- Dado que exista uma tarefa cadastrada;

\- Quando o usuário solicitar sua exclusão e confirmar a operação;

\- Então o sistema deve remover o registro e atualizar a listagem.



\*\*Cenário 2 — Cancelar exclusão\*\*



\- Dado que o usuário tenha solicitado a exclusão de uma tarefa;

\- Quando cancelar a confirmação;

\- Então o sistema deve manter a tarefa cadastrada.



\*\*Cenário 3 — Tentar excluir tarefa inexistente\*\*



\- Dado que o identificador informado não corresponda a uma tarefa cadastrada;

\- Quando o sistema tentar localizar o registro para exclusão;

\- Então deve apresentar uma mensagem informando que a tarefa não foi encontrada.



\### US05 — Alterar status das tarefas



\*\*História:\*\*



Como usuário, quero alterar o status de uma tarefa entre pendente e concluída para acompanhar meu progresso.



\*\*Requisito relacionado:\*\* RF08.



\*\*Caso de uso relacionado:\*\* UC05.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Concluir tarefa pendente\*\*



\- Dado que exista uma tarefa com status pendente;

\- Quando o usuário selecionar a opção de concluir;

\- Então o sistema deve alterar seu status para concluída e atualizar a informação no banco de dados.



\*\*Cenário 2 — Retornar tarefa ao status pendente\*\*



\- Dado que exista uma tarefa com status concluída;

\- Quando o usuário selecionar a opção de reabrir;

\- Então o sistema deve alterar seu status para pendente.



\*\*Cenário 3 — Atualizar indicação de atraso\*\*



\- Dado que uma tarefa esteja concluída e possua data de vencimento anterior à data atual;

\- Quando o usuário visualizar a tarefa;

\- Então o sistema não deve identificá-la como atrasada.



\### US06 — Filtrar tarefas



\*\*História:\*\*



Como usuário, quero filtrar minhas tarefas por status e prioridade para encontrar rapidamente as atividades que preciso realizar.



\*\*Requisitos relacionados:\*\* RF09 e RF10.



\*\*Caso de uso relacionado:\*\* UC06.



\*\*Critérios de aceite:\*\*



\*\*Cenário 1 — Filtrar por status\*\*



\- Dado que existam tarefas com diferentes status;

\- Quando o usuário selecionar o filtro pendente;

\- Então o sistema deve apresentar somente as tarefas pendentes.



\*\*Cenário 2 — Filtrar por prioridade\*\*



\- Dado que existam tarefas com diferentes prioridades;

\- Quando o usuário selecionar a prioridade alta;

\- Então o sistema deve apresentar somente as tarefas classificadas com prioridade alta.



\*\*Cenário 3 — Combinar filtros\*\*



\- Dado que existam tarefas com diferentes prioridades e status;

\- Quando o usuário selecionar simultaneamente um status e uma prioridade;

\- Então o sistema deve apresentar somente as tarefas que atendam aos dois critérios.



\*\*Cenário 4 — Remover filtros\*\*



\- Dado que exista um filtro aplicado;

\- Quando o usuário selecionar a opção de limpar filtros;

\- Então o sistema deve apresentar novamente todas as tarefas cadastradas.



\*\*Cenário 5 — Nenhum resultado encontrado\*\*



\- Dado que existam tarefas cadastradas;

\- Quando o usuário aplicar filtros sem correspondência;

\- Então o sistema deve apresentar uma mensagem informando que nenhuma tarefa foi encontrada.



\## 3. Matriz de rastreabilidade



| História | Requisitos funcionais | Caso de uso |

|---|---|---|

| US01 | RF01, RF06, RF07 | UC01 |

| US02 | RF02, RF03, RF11 | UC02 |

| US03 | RF04, RF06, RF07 | UC03 |

| US04 | RF05 | UC04 |

| US05 | RF08 | UC05 |

| US06 | RF09, RF10 | UC06 |



\## 4. Considerações finais



As histórias de usuário e seus respectivos critérios de aceite estabelecem as condições necessárias para validar as funcionalidades do Tarefaê.



Esses critérios servirão como referência para o desenvolvimento, elaboração dos testes automatizados e acompanhamento das Issues no GitHub.



Uma funcionalidade somente deverá ser considerada concluída quando atender aos critérios de aceite definidos para sua respectiva história.

