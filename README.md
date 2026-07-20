# Data Platform 360

Projeto desenvolvido para estudar e praticar Engenharia de Dados, simulando a construção de uma plataforma de dados utilizada em ambientes corporativos.

O objetivo é evoluir continuamente o projeto, passando desde conceitos básicos de SQL até pipelines completos utilizando Airflow, Spark, dbt, BigQuery e Google Cloud.

---

# Objetivos

Este projeto tem como finalidade:

- praticar Engenharia de Dados na prática;
- aprender SQL de forma profissional;
- desenvolver pipelines de dados;
- aplicar boas práticas de versionamento;
- documentar todo o aprendizado;
- construir um portfólio técnico.

---

# Tecnologias

Atualmente o projeto utiliza:

- PostgreSQL
- Docker
- Docker Compose
- Git
- SQL

Tecnologias previstas para as próximas etapas:

- Python
- Apache Airflow
- Apache Spark
- dbt
- BigQuery
- Google Cloud Storage
- Terraform

---

# Estrutura do Projeto

```
data-platform-360/

├── architecture/        # Diagramas e arquitetura
├── datasets/            # Arquivos CSV para estudos
├── docker/              # Arquivos auxiliares do Docker
├── docs/                # Documentação
├── notebooks/           # Estudos exploratórios
├── spark/               # Projetos Spark
├── sql/
│   ├── schema/          # Criação das tabelas
│   ├── seeds/           # Dados iniciais
│   └── queries/         # Consultas SQL
├── src/                 # Código Python
├── tests/               # Testes
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

# Pré-requisitos

Antes de iniciar, instale:

- Git
- Docker Desktop
- PostgreSQL (opcional)
- DBeaver (recomendado)

---

# Clonando o projeto

```bash
git clone https://github.com/tiagors/data-platform-360.git

cd data-platform-360
```


## Configuração do ambiente

1. Clone o repositório.
2. Crie o ambiente virtual:
   ```
   python -m venv .venv
```

3. Ative o ambiente virtual.
4. Instale as dependências:
    
    ```
    pip install -r requirements.txt
    ```
    
5. Execute o script de validação do ambiente:
    
    ```
    python src/test_environment.py
    ```


---

# Executando o ambiente

Suba os containers:

```bash
docker compose up -d
```

Verifique se o container está em execução:

```bash
docker ps
```

Parar os containers:

```bash
docker compose down
```

---

# Configuração do PostgreSQL

Após subir o Docker:

Servidor

```
localhost
```

Porta

```
5432
```

Banco

```
data_platform
```

Usuário

```
data_engineer
```

Senha

```
data123
```

> **Importante:** essas credenciais são utilizadas apenas para ambiente de desenvolvimento. Em produção elas deverão ser armazenadas em variáveis de ambiente.

---

# Criando as tabelas

Executar os scripts localizados em:

```
sql/schema/
```

Depois executar:

```
sql/seeds/
```

---

# Executando consultas

Os exemplos estão em:

```
sql/queries/
```

ou

```
sql/basic_queries.sql
```

---

# Fluxo de Desenvolvimento

Sempre utilize o seguinte fluxo:

1. Criar uma branch

```bash
git checkout -b feature/nome-da-feature
```

2. Fazer alterações

3. Verificar

```bash
git status
```

4. Revisar

```bash
git diff
```

5. Commit

```bash
git add .

git commit -m "feat: descrição"
```

6. Enviar

```bash
git push origin feature/nome-da-feature
```

---

# Convenções

## Commits

Utilizamos Conventional Commits.

Exemplos:

```
feat:
fix:
docs:
refactor:
test:
style:
chore:
```

---

## SQL

Padrão utilizado:

- palavras-chave em maiúsculo;
- indentação com quatro espaços;
- uma coluna por linha;
- aliases explícitos.

Exemplo:

```sql
SELECT
    product_name,
    price
FROM products
WHERE price > 100
ORDER BY price DESC;
```

---

## Python

Seguimos:

- PEP8
- Black
- Ruff
- Type Hints

---

# Roadmap

## Concluído

- [x] Git
- [x] Docker
- [x] PostgreSQL
- [x] SQL Básico

## Em andamento

- [ ] Joins
- [ ] Views
- [ ] Procedures

## Próximos módulos

- [ ] Python
- [ ] ETL
- [ ] Airflow
- [ ] Spark
- [ ] dbt
- [ ] BigQuery
- [ ] Google Cloud

---

# Documentação

Documentação adicional:

```
docs/
```

Arquitetura:

```
architecture/
```

---

# Licença

Projeto desenvolvido exclusivamente para fins de estudo.

---

# Autor

Tiago Ricardo da Silva

LinkedIn:

https://www.linkedin.com/in/tiagors/

GitHub:

https://github.com/tiagors