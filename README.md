# Data Platform 360

## Objetivo

Construir uma plataforma moderna de Engenharia de Dados durante 16 semanas, simulando um ambiente corporativo.

## Tecnologias

- Python
- PostgreSQL
- Docker
- Airflow
- Google Cloud
- BigQuery
- PySpark
- dbt
- Looker Studio
- Git
- GitHub

## Estrutura do Projeto

├───.github
├───architecture
├───datasets
├───dbt
├───docker
├───docker-compose.yml
├───docs
├───images
├───logs
├───notebooks
├───requirements.txt
├───scripts
├───spark
├───sql
├───src
└───tests

## Infraestrutura Local
Os serviços serão executados via Docker ao longo do projeto.

## Roadmap

- Sprint 0 ✅
    Dia 1 ✅ – Ambiente Python
    Dia 2 ✅ – Repositório Profissional
    Dia 3 ✅ – Docker
    Dia 4 ✅ – PostgreSQL Local
    Dia 5 ✅ – Data Engineering Second Brain

- Sprint 1 ⏳
    Dia 1
- Sprint 2 ⏳

## Arquitetura Atual
Python
   │
PostgreSQL (Docker)

## Fluxo de Desenvolvimento
Este projeto utiliza Git como ferramenta de versionamento.

Fluxo adotado:

1. Criar uma branch para cada tarefa.
2. Desenvolver pequenas alterações.
3. Criar commits semânticos.
4. Publicar no GitHub.


## Modelo de Dados Inicial

A primeira versão da plataforma utiliza o PostgreSQL como camada de armazenamento.

### Tabelas

- `customers`
- `products` (exercício)

Os scripts SQL estão organizados em:

- `sql/schema/`
- `sql/seeds/`
- `sql/queries/`

## Status

Em desenvolvimento.