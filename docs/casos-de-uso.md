# Casos de Uso — Tarefaê



**Versão:** 1.0.0

**Data:** 06/11/2026

**Status:** Em especificação



## 1. Introdução



Este documento apresenta a especificação dos casos de uso da aplicação Tarefaê, descrevendo as interações entre o usuário e o sistema para a realização das principais operações de gerenciamento de tarefas.



Os casos de uso foram elaborados com base nos requisitos funcionais definidos em `docs/requisitos.md`.



## 2. Atores



### 2.1. Usuário



Pessoa que utiliza a aplicação para organizar suas atividades cotidianas. Pode cadastrar, consultar, editar, excluir, filtrar e alterar o status das tarefas.



### 2.2. Sistema



Componente responsável por processar as solicitações do usuário, validar informações, executar as operações e armazenar os dados no banco de dados SQLite.



## 3. Lista de casos de uso



| ID | Caso de uso | Requisitos relacionados |

|---|---|---|

| UC01 | Cadastrar tarefa | RF01, RF06, RF07 |

| UC02 | Consultar tarefas e detalhes | RF02, RF03, RF11 |

| UC03 | Editar tarefa | RF04, RF06, RF07 |

| UC04 | Excluir tarefa | RF05 |

| UC05 | Alterar status | RF08 |

| UC06 | Filtrar tarefas | RF09, RF10 |



---



## 4. Especificação dos casos de uso



### UC01 — Cadastrar tarefa



**Objetivo:** Permitir que o usuário registre uma nova tarefa no sistema.



**Ator principal:** Usuário.



**Pré-condições:**

- A aplicação deve estar disponível.

- O formulário de cadastro deve estar acessível.



**Fluxo principal:**

1. O usuário acessa a opção de cadastrar tarefa.

2. O sistema apresenta o formulário de cadastro.

3. O usuário informa o título da tarefa.

4. O usuário informa opcionalmente a descrição.

5. O usuário seleciona a prioridade.

6. O usuário informa opcionalmente a data de vencimento.

7. O usuário confirma o cadastro.

8. O sistema valida as informações.

9. O sistema atribui o status pendente e, caso não tenha sido selecionada, a prioridade média.

10. O sistema salva a tarefa no banco de dados.

11. O sistema apresenta uma mensagem de confirmação.



**Fluxos alternativos:**

- A1: O usuário não informa a descrição. O sistema permite continuar o cadastro.

- A2: O usuário não informa a data de vencimento. O sistema permite continuar o cadastro.

- A3: O usuário não seleciona uma prioridade. O sistema atribui a prioridade média.



**Fluxos de exceção:**

- E1: O usuário tenta cadastrar uma tarefa sem título. O sistema apresenta uma mensagem informando que o campo é obrigatório.

- E2: O usuário informa dados inválidos. O sistema apresenta mensagens de validação e não realiza o cadastro.

- E3: Ocorre uma falha no armazenamento. O sistema informa que não foi possível salvar a tarefa.



**Pós-condições:**

- A tarefa é armazenada no banco de dados com status pendente.



### UC02 — Consultar tarefas e detalhes



**Objetivo:** Permitir que o usuário visualize as tarefas cadastradas e consulte suas informações.



**Ator principal:** Usuário.



**Pré-condições:**

- A aplicação deve estar disponível.



**Fluxo principal:**

1. O usuário acessa a página principal.

2. O sistema consulta as tarefas armazenadas.

3. O sistema apresenta a lista de tarefas.

4. O usuário seleciona uma tarefa.

5. O sistema apresenta os detalhes da tarefa, incluindo título, descrição, prioridade, status, data de criação e data de vencimento.

6. O sistema identifica visualmente se a tarefa está atrasada.



**Fluxos alternativos:**

- A1: Não existem tarefas cadastradas. O sistema apresenta uma mensagem informando que a lista está vazia.

- A2: O usuário consulta a lista sem selecionar uma tarefa específica. O sistema mantém a visualização geral.



**Fluxos de exceção:**

- E1: Ocorre uma falha na consulta ao banco de dados. O sistema informa que não foi possível carregar as tarefas.

- E2: O usuário solicita os detalhes de uma tarefa inexistente. O sistema informa que o registro não foi encontrado.



**Pós-condições:**

- As informações das tarefas são apresentadas sem alteração dos registros.



### UC03 — Editar tarefa



**Objetivo:** Permitir que o usuário atualize as informações de uma tarefa existente.



**Ator principal:** Usuário.



**Pré-condições:**

- A tarefa deve estar cadastrada no sistema.

- A aplicação deve estar disponível.



**Fluxo principal:**

1. O usuário acessa a lista de tarefas.

2. O usuário seleciona a tarefa que deseja editar.

3. O sistema apresenta o formulário preenchido com os dados atuais.

4. O usuário altera as informações desejadas.

5. O usuário confirma a edição.

6. O sistema valida os dados informados.

7. O sistema atualiza o registro no banco de dados.

8. O sistema apresenta uma mensagem de confirmação.



**Fluxos alternativos:**

- A1: O usuário mantém algum campo opcional sem preenchimento. O sistema permite salvar as alterações.

- A2: O usuário cancela a edição. O sistema retorna à visualização anterior sem salvar as alterações.



**Fluxos de exceção:**

- E1: O usuário remove o título obrigatório. O sistema impede a atualização e apresenta uma mensagem de validação.

- E2: Ocorre uma falha no banco de dados. O sistema informa que não foi possível atualizar a tarefa.

- E3: A tarefa não é encontrada. O sistema informa que o registro não existe.



**Pós-condições:**

- As alterações confirmadas são armazenadas no banco de dados.



### UC04 — Excluir tarefa



**Objetivo:** Permitir que o usuário remova uma tarefa cadastrada.



**Ator principal:** Usuário.



**Pré-condições:**

- A tarefa deve existir no sistema.



**Fluxo principal:**

1. O usuário acessa a lista de tarefas.

2. O usuário seleciona a tarefa que deseja excluir.

3. O sistema solicita a confirmação da exclusão.

4. O usuário confirma a operação.

5. O sistema remove o registro do banco de dados.

6. O sistema atualiza a listagem.

7. O sistema apresenta uma mensagem de confirmação.



**Fluxos alternativos:**

- A1: O usuário cancela a exclusão. O sistema mantém o registro sem alterações.



**Fluxos de exceção:**

- E1: A tarefa não é encontrada. O sistema informa que não foi possível localizar o registro.

- E2: Ocorre uma falha na exclusão. O sistema informa que não foi possível concluir a operação.



**Pós-condições:**

- A tarefa excluída deixa de aparecer na listagem e não permanece disponível para consulta.



### UC05 — Alterar status



**Objetivo:** Permitir que o usuário altere o status de uma tarefa entre pendente e concluída.



**Ator principal:** Usuário.



**Pré-condições:**

- A tarefa deve estar cadastrada no sistema.



**Fluxo principal:**

1. O usuário acessa a lista de tarefas.

2. O usuário seleciona a opção de alteração de status.

3. O sistema identifica o status atual.

4. O sistema altera o status para o valor correspondente.

5. O sistema salva a alteração no banco de dados.

6. O sistema atualiza a apresentação da tarefa.



**Fluxos alternativos:**

- A1: A tarefa está pendente. O sistema permite marcá-la como concluída.

- A2: A tarefa está concluída. O sistema permite retorná-la ao status pendente.



**Fluxos de exceção:**

- E1: A tarefa não é encontrada. O sistema informa que o registro não existe.

- E2: Ocorre uma falha na atualização. O sistema informa que não foi possível alterar o status.



**Pós-condições:**

- O novo status da tarefa permanece armazenado no banco de dados.



### UC06 — Filtrar tarefas



**Objetivo:** Permitir que o usuário encontre tarefas de acordo com seu status ou prioridade.



**Ator principal:** Usuário.



**Pré-condições:**

- A aplicação deve estar disponível.



**Fluxo principal:**

1. O usuário acessa a lista de tarefas.

2. O sistema apresenta as opções de filtragem.

3. O usuário seleciona um filtro de status ou prioridade.

4. O sistema processa a solicitação.

5. O sistema apresenta somente as tarefas correspondentes aos critérios selecionados.



**Fluxos alternativos:**

- A1: O usuário seleciona apenas o filtro de status.

- A2: O usuário seleciona apenas o filtro de prioridade.

- A3: O usuário combina filtros de status e prioridade.

- A4: O usuário remove os filtros. O sistema apresenta novamente todas as tarefas.



**Fluxos de exceção:**

- E1: Nenhuma tarefa corresponde aos filtros selecionados. O sistema apresenta uma mensagem informando que não foram encontradas tarefas.

- E2: Ocorre uma falha na consulta. O sistema informa que não foi possível aplicar os filtros.



**Pós-condições:**

- A lista é apresentada de acordo com os critérios selecionados, sem modificar os registros armazenados.



---



## 5. Considerações finais



Os casos de uso apresentados descrevem as principais interações previstas para a primeira versão do Tarefaê.



A especificação servirá como referência para a implementação das funcionalidades, elaboração dos testes e validação dos critérios de aceite.



Os fluxos descritos deverão permanecer alinhados aos requisitos funcionais e às histórias de usuário do projeto.

