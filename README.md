# receitas-api
# receitas-api

Uma API de receitas desenvolvida para facilitar o gerenciamento, consulta e sugestão de receitas culinárias. O projeto foi criado como parte da disciplina de Qualidade de Software, com foco em boas práticas de desenvolvimento, escalabilidade e integração de serviços.

## Tecnologias Utilizadas

- **Django**: Framework principal para desenvolvimento web.
- **Django REST Framework (DRF)**: Utilizado para criação de endpoints RESTful.
- **PostgreSQL**: Banco de dados relacional para armazenamento das receitas e usuários.
- **Celery**: Gerenciador de tarefas assíncronas, utilizado para atualizar receitas sugeridas periodicamente.

## Funcionalidades

- Cadastro, consulta, atualização e remoção de receitas.
- Sugestão automática de receitas utilizando tarefas assíncronas.
- API RESTful para integração com frontends ou outros serviços.