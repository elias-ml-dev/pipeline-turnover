# Fluxo do Projeto – Pipeline Turnover

## 1. Objetivo

Desenvolver um projeto de Engenharia de Dados utilizando uma base de dados de funcionários para construir um pipeline ETL, realizar análises e posteriormente aplicar técnicas de Machine Learning.

## 2. Etapas do projeto

### 2.1. Análise exploratória inicial (EDA)

Antes da construção do pipeline, foi realizada uma exploração inicial da base para compreender sua estrutura e qualidade.

Foram verificadas:
- Quantidade de registros e colunas;
- Tipos de dados;
- Valores ausentes;
- Registros duplicados;
- Distribuição da variável de saída dos funcionários.

Essa etapa permite conhecer os dados antes de definir as transformações necessárias.

### 2.2. Engenharia de Dados (ETL)

Será desenvolvido um processo ETL utilizando Python:

- **Extract:** extração dos dados da base original em CSV.
- **Transform:** limpeza, validação e padronização dos dados.
- **Load:** carregamento dos dados tratados em um banco de dados.

### 2.3. Análise de Dados

Após o processamento e carregamento, serão realizadas análises utilizando os dados tratados, buscando identificar padrões e indicadores relacionados ao turnover.

### 2.4. Machine Learning

Posteriormente, será desenvolvido um modelo de Machine Learning para investigar padrões associados à saída de funcionários.

## 3. Tecnologias planejadas

- Python e Pandas;
- Banco de dados SQL;
- Docker;
- Apache Airflow;
- Databricks (a avaliar);
- Scikit-learn.

## 4. Fluxo geral

Base original → Análise exploratória inicial → ETL → Banco de dados → Análise de Dados → Machine Learning.

**Observação:** Docker, Airflow e Databricks serão avaliados e incorporados conforme a evolução do projeto e as necessidades identificadas.