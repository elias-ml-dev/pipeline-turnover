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

## 2.2. Engenharia de Dados (ETL)

Está sendo desenvolvido um processo ETL utilizando Python e Pandas.

**Extract:** extração dos dados da base original em CSV, realizada por meio de uma função Python.

**Transform:** limpeza, validação e padronização dos dados.

Transformações já implementadas:
- Conversão das colunas com respostas Sim/Não para valores binários (0 e 1).
- Aplicação de One-Hot Encoding nas colunas Estado Civil, Frequência de Viagens e Formação.
- Aplicação de codificação ordinal nas colunas E-Sat e Equilíbrio de Vida.
- Conversão da coluna Gênero para valores numéricos (H = 0 e M = 1).

Próximas etapas:
- Implementar validações adicionais de consistência dos dados.
- Avaliar novas transformações conforme as necessidades da análise.
- Integrar as etapas do ETL por meio do arquivo `main.py`.

**Load:** carregamento dos dados transformados em um banco de dados MySQL, utilizando SQLAlchemy e PyMySQL.

Implementações realizadas:
- Configuração da conexão com o MySQL por meio de variáveis de ambiente (`python-dotenv`).
- Exportação dos dados processados para um arquivo CSV.
- Criação e carregamento da tabela `funcionarios` no banco `db_turnover`.
- Testes de conexão e conferência dos registros carregados.

Resultado inicial:
- 1.470 registros carregados.
- 29 colunas na tabela `funcionarios`.
- Carga testada com sucesso.

### 2.3. Análise de Dados

Após o processamento e carregamento, serão realizadas análises utilizando SQL e Python (Pandas), buscando identificar padrões e indicadores relacionados ao turnover.

Também serão reproduzidas e ampliadas as análises exploratórias inicialmente realizadas no Excel.

### 2.4. Machine Learning

Posteriormente, será desenvolvido um modelo de Machine Learning para investigar padrões associados à saída de funcionários.

## 3. Tecnologias utilizadas e planejadas

- Python;
- Pandas;
- SQLAlchemy;
- PyMySQL;
- python-dotenv;
- MySQL;
- Docker;
- Apache Airflow;
- Scikit-learn;

**## 4. Fluxo geral**

Base original → Análise exploratória inicial → Extração → Transformação → Carga no MySQL → Análise de Dados → Machine Learning → Dashboard.

**Observação:** o pipeline ETL já possui as etapas de extração, transformação e carga implementadas individualmente e testadas. A integração dessas etapas pelo `main.py` ainda está pendente. Docker e Apache Airflow serão incorporados em etapas futuras para containerização e orquestração do pipeline, respectivamente. Databricks permanece como tecnologia a avaliar.