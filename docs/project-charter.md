# Project Charter — Tarefaê



**Projeto:** Tarefaê — Gerenciador de Tarefas

**Versão do documento:** 1.0

**Status:** Em desenvolvimento

**Responsável pelo projeto:** Susana Teixeira Mota

**Repositório:** [github.com/ScatachM/tarefae](https://github.com/ScatachM/tarefae)



---



## 1. Justificativa e visão geral do produto



O Tarefaê é uma aplicação web desenvolvida para facilitar a organização e o acompanhamento de tarefas pessoais, acadêmicas e profissionais.



A proposta surgiu da necessidade de centralizar atividades em um ambiente simples e intuitivo, permitindo que os usuários registrem suas tarefas, organizem prioridades, acompanhem prazos e visualizem o andamento das atividades.



A aplicação oferece recursos para cadastro, consulta, edição e exclusão de tarefas, definição de prioridades e datas de vencimento, acompanhamento de status e identificação visual de atividades atrasadas.



O produto busca proporcionar uma experiência simples e intuitiva, por meio de uma interface responsiva e da persistência das informações em banco de dados relacional.


O desenvolvimento também tem como finalidade aplicar práticas de Engenharia de Software, incluindo especificação de requisitos, modelagem de dados, versionamento, gerenciamento de atividades e testes automatizados.



## 2. Objetivos SMART



Os objetivos do projeto foram definidos considerando critérios de especificidade, mensuração, viabilidade, relevância e prazo.



| Identificação | Objetivo | Indicador de sucesso |

|---|---|---|

| OBJ01 | Desenvolver uma aplicação web para gerenciamento de tarefas. | Aplicação executável utilizando Flask. |

| OBJ02 | Implementar as operações fundamentais de gerenciamento de tarefas. | Cadastro, listagem, edição e exclusão funcionais. |

| OBJ03 | Permitir a organização e o acompanhamento das atividades. | Prioridade, status, vencimento e filtros implementados. |

| OBJ04 | Identificar visualmente tarefas atrasadas. | Tarefas pendentes com vencimento anterior à data atual destacadas na interface. |

| OBJ05 | Garantir a persistência das informações. | Dados armazenados em banco SQLite e preservados entre execuções. |

| OBJ06 | Validar o funcionamento das funcionalidades principais. | Pelo menos 10 testes automatizados executados com sucesso no MVP. |

| OBJ07 | Documentar e organizar o desenvolvimento. | Documentos de engenharia, Issues, branches e Pull Requests registrados no GitHub. |



**Prazo:** os objetivos deverão ser cumpridos até o encerramento da atividade acadêmica. A validação será realizada por meio da execução das funcionalidades, dos testes automatizados e da integração das alterações ao repositório, respeitando o fluxo de branches e Pull Requests.



## 3. Escopo do projeto



### 3.1. Dentro do escopo do MVP



O MVP contempla:



- Desenvolvimento de uma aplicação web utilizando Python e Flask.

- Interface construída com HTML5 e CSS3.

- Interface responsiva para diferentes tamanhos de tela.

- Cadastro de tarefas com título e descrição.

- Listagem das tarefas cadastradas.

- Edição das informações das tarefas.

- Exclusão de tarefas.

- Definição de prioridade: baixa, média e alta.

- Definição de status: pendente e concluída.

- Definição de datas de vencimento.

- Filtragem de tarefas por status e prioridade.

- Identificação visual de tarefas atrasadas.

- Persistência dos dados utilizando SQLite.

- Validação de campos obrigatórios e informações fornecidas.

- Implementação de testes automatizados com pytest.

- Documentação técnica e gerenciamento do projeto com Git e GitHub.



### 3.2. Fora do escopo do MVP



Não fazem parte da primeira versão:



- Cadastro e autenticação de usuários.

- Gerenciamento de múltiplos perfis.

- Compartilhamento de tarefas entre usuários.

- Categorias e etiquetas personalizadas.

- Notificações automáticas de vencimento.

- Integração com calendários externos.

- Aplicativo nativo para dispositivos móveis.

- Painéis avançados de estatísticas e produtividade.

- Sincronização em nuvem entre dispositivos.



Essas funcionalidades poderão ser avaliadas em versões futuras, conforme a evolução do projeto.



## 4. Stakeholders e público-alvo



### 4.1. Stakeholders



| Stakeholder | Responsabilidade ou interesse |

|---|---|

| Desenvolvedora | Planejamento, especificação, implementação, testes e manutenção do sistema. |

| Professor avaliador | Avaliação técnica, orientação e acompanhamento da evolução do projeto. |

| Usuários finais | Utilização da aplicação para organização e acompanhamento de tarefas. |



### 4.2. Público-alvo



O Tarefaê é destinado a pessoas que precisam organizar atividades pessoais, acadêmicas ou profissionais, especialmente estudantes e profissionais que desejam acompanhar tarefas, prioridades e prazos em uma ferramenta simples.



## 5. Requisitos de alto nível



O projeto deve atender aos seguintes requisitos gerais:



- Disponibilizar operações de gerenciamento de tarefas.

- Permitir organização por prioridade e status.

- Armazenar os dados de maneira persistente.

- Identificar tarefas com prazo vencido.

- Disponibilizar interface responsiva e intuitiva.

- Manter a consistência das informações cadastradas.

- Possibilitar a execução de testes automatizados.



A especificação detalhada encontra-se em [docs/requisitos.md](requisitos.md).



## 6. Premissas e restrições



### 6.1. Premissas



- O usuário possui acesso a um navegador web atualizado.

- O ambiente de execução possui Python instalado.

- A aplicação será executada localmente durante a validação do MVP.

- O banco SQLite será utilizado para armazenamento das informações.

- O escopo será mantido enxuto para permitir a conclusão dentro do período acadêmico estabelecido.



### 6.2. Restrições



- O desenvolvimento utiliza Python e Flask.

- A persistência utiliza SQLite.

- O projeto é desenvolvido individualmente.

- O prazo é limitado ao ciclo acadêmico da atividade.

- O MVP não contempla autenticação ou gerenciamento de múltiplos usuários.

- O controle de versão e a integração das funcionalidades seguem o fluxo Git adotado no repositório.



## 7. Critérios de sucesso e aceitação



O MVP será considerado concluído quando:



1. A aplicação puder ser iniciada e acessada por navegador.

2. O usuário conseguir cadastrar, visualizar, editar e excluir tarefas.

3. As tarefas puderem ser organizadas por prioridade e status.

4. As datas de vencimento forem armazenadas e exibidas corretamente.

5. Os filtros por status e prioridade funcionarem.

6. As tarefas atrasadas forem identificadas visualmente.

7. Os dados permanecerem armazenados no SQLite.

8. Os testes automatizados previstos para o MVP forem executados com sucesso.

9. A documentação técnica estiver disponível no repositório.

10. O código estiver integrado à branch `main` por meio de Pull Requests aprovados, seguindo o fluxo de desenvolvimento estabelecido.



## 8. Estratégia de desenvolvimento



O desenvolvimento utiliza uma abordagem incremental, dividindo o trabalho em unidades menores representadas por Issues no GitHub.



O controle de versão segue uma versão simplificada do Git Flow:



- `main`: versões estáveis.

- `develop`: integração das funcionalidades.

- `feature/*` e outras branches temáticas: implementação de atividades específicas.



As alterações são registradas utilizando Conventional Commits e integradas por Pull Requests vinculados às respectivas Issues.



O versionamento das versões estáveis segue Semantic Versioning (SemVer).



## 9. Tecnologias previstas



| Tecnologia | Finalidade |

|---|---|

| Python 3 | Linguagem principal |

| Flask | Framework web |

| SQLite | Banco de dados |

| HTML5 | Estrutura da interface |

| CSS3 | Estilização e responsividade |

| Pytest | Testes automatizados |

| Git | Controle de versão |

| GitHub | Hospedagem e gerenciamento do projeto |



## 10. Riscos iniciais



| Risco | Impacto | Estratégia de mitigação |

|---|---|---|

| Ampliação excessiva do escopo | Atraso na entrega | Priorizar funcionalidades essenciais do MVP. |

| Perda ou inconsistência de dados | Comprometimento das informações | Utilizar persistência SQLite e validar operações. |

| Falhas nas funcionalidades | Problemas de utilização | Implementar testes automatizados. |

| Problemas de integração | Conflitos no desenvolvimento | Utilizar branches temáticas e Pull Requests. |

| Documentação desatualizada | Perda de rastreabilidade | Atualizar documentos conforme a evolução do sistema. |



## 11. Aprovação e encerramento



Este Project Charter formaliza a proposta, os objetivos, o escopo e as diretrizes iniciais do desenvolvimento do Tarefaê. Sua revisão e validação fazem parte do processo de documentação e acompanhamento acadêmico do projeto.



O documento serve como referência para orientar as decisões de implementação, controlar alterações de escopo e avaliar a evolução do produto ao longo dos ciclos de desenvolvimento.



**Responsável:** Susana Teixeira Mota

**Projeto:** Tarefaê — Gerenciador de Tarefas

