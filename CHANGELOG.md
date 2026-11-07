# Changelog



Todas as alterações relevantes do Tarefaê serão documentadas neste arquivo.



O formato segue as recomendações do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/), e o projeto utiliza [Semantic Versioning](https://semver.org/lang/pt-BR/).



## [Unreleased]



### Added

- Integração contínua com GitHub Actions para execução automatizada dos testes.

- Medição de cobertura de código com pytest-cov, estabelecendo o mínimo de 80%.

- Documentação da arquitetura do sistema.

- Matriz de rastreabilidade entre requisitos, histórias de usuário, casos de uso, Issues e testes.

- Licença MIT para distribuição open source do projeto.



### Changed

- Correção da formatação Markdown nos documentos de engenharia.

- Atualização da documentação do projeto e dos requisitos.

- Atualização da suíte de testes para contemplar a proteção CSRF.



### Security

- Implementação de proteção CSRF nos formulários de cadastro, edição e exclusão de tarefas.

- Configuração de chave secreta por variável de ambiente.

- Adição de testes para verificar o bloqueio de requisições sem token CSRF válido.



## [0.2.0] - 2026-11-06



### Added

- Estrutura inicial da aplicação web com Flask.

- Persistência de dados utilizando SQLite.

- Cadastro e listagem de tarefas.

- Edição e exclusão de tarefas.

- Definição de prioridades: baixa, média e alta.

- Definição de datas de vencimento.

- Controle de status: pendente e concluída.

- Filtros de tarefas por status e prioridade.

- Identificação visual de tarefas atrasadas.

- Interface responsiva.

- Testes automatizados com pytest.

- Documentação inicial do projeto, incluindo requisitos, casos de uso, histórias de usuário e modelo de dados.

- README com instruções de instalação e execução.



[Unreleased]: https://github.com/ScatachM/tarefae/compare/v0.2.0...HEAD

[0.2.0]: https://github.com/ScatachM/tarefae/releases/tag/v0.2.0

