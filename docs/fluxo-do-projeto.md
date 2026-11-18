# Fluxo do Projeto – Pipeline Turnover

## 1. Objetivo

Desenvolver um projeto de Engenharia de Dados utilizando uma base de dados de funcionários para construir um pipeline ETL, realizar análises e posteriormente aplicar técnicas de Machine Learning.

## 2. Etapas do projeto

### 2.1. Análise Exploratória Inicial (EDA)

Antes da construção do pipeline, foi realizada uma exploração inicial da base para compreender sua estrutura e qualidade.

Foram verificadas:
- Quantidade de registros e colunas;
- Tipos de dados;
- Valores ausentes;
- Registros duplicados;
- Distribuição da variável de saída dos funcionários.

Essa etapa permite conhecer os dados antes de definir as transformações necessárias.

### 2.2. Engenharia de Dados (ETL)

Foi desenvolvido um processo ETL utilizando Python e Pandas, dividido em três etapas: Extract, Transform e Load.

**Extract:**

Extração dos dados da base original em CSV, realizada por meio de uma função Python.

Implementações realizadas:
- Leitura do arquivo `tech_employees.csv`;
- Configuração do separador `;`;
- Desconsideração das duas primeiras linhas do arquivo;
- Preservação da base original na pasta `data/raw/`.

**Transform:**

Limpeza, codificação e transformação dos dados para prepará-los para análises posteriores.

Transformações implementadas:
- Conversão das colunas com respostas Sim/Não para valores binários (0 e 1);
- Aplicação de One-Hot Encoding nas colunas Estado Civil, Frequência de Viagens e Formação;
- Aplicação de codificação ordinal nas colunas E-Sat e Equilíbrio de Vida;
- Conversão da coluna Gênero para valores numéricos (H = 0 e M = 1).

**Validações de qualidade implementadas:**

1. Verificação de identificadores únicos (IDs);
2. Verificação de valores ausentes;
3. Verificação de registros duplicados;
4. Verificação da integridade da variável-alvo `Funcionário_deixou_a_empresa`, permitindo apenas 0 e 1;
5. Verificação da faixa de idade, entre 18 e 60 anos;
6. Verificação de salários maiores que zero;
7. Verificação de quantidade de empresas trabalhadas maior ou igual a zero;
8. Verificação de tempo de empresa maior ou igual a zero;
9. Verificação de anos no mesmo cargo maior ou igual a zero;
10. Verificação de anos desde a última promoção maior ou igual a zero;
11. Verificação de anos com o mesmo chefe maior ou igual a zero.

As validações utilizam condições e exceções (`raise ValueError`) para interromper o processamento quando alguma regra não é atendida.

**Resultado após a transformação:**
- 1.470 registros;
- 29 colunas;
- Nenhum valor ausente;
- Nenhum registro duplicado;
- Todas as validações implementadas aprovadas nos testes realizados.

**Load:**

Carregamento dos dados transformados em um banco de dados MySQL, utilizando SQLAlchemy e PyMySQL.

Implementações realizadas:
- Configuração da conexão com o MySQL por meio de variáveis de ambiente, utilizando `python-dotenv`;
- Exportação dos dados processados para um arquivo CSV na pasta `data/processed/`;
- Criação e carregamento da tabela `funcionarios` no banco `db_turnover`;
- Testes de conexão e conferência dos registros carregados.

**Resultado da carga:**
- 1.470 registros carregados;
- 29 colunas na tabela `funcionarios`;
- Carga testada com sucesso.

### 2.3. Integração do Pipeline

As etapas de extração, transformação e carga foram integradas no arquivo `main.py`, responsável por coordenar a execução do processo ETL.

Implementações realizadas:
- Importação das funções de cada etapa do ETL;
- Organização da sequência de execução;
- Criação da função principal `pipeline()`;
- Inclusão de mensagens para acompanhar o andamento da execução;
- Utilização do bloco `if __name__ == "__main__":` para iniciar o processo.

A execução completa é realizada por meio do comando:

`python -m pipeline.main`

O funcionamento foi testado com sucesso, executando as três etapas em sequência.

### 2.4. Análise de Dados

Após o processamento e carregamento, serão realizadas análises utilizando SQL e Python (Pandas), buscando identificar padrões e indicadores relacionados ao turnover.

Também serão reproduzidas e ampliadas as análises exploratórias inicialmente realizadas no Excel.

### 2.5. Machine Learning

Posteriormente, será desenvolvido um modelo de Machine Learning para investigar padrões associados à saída de funcionários.

Será utilizada a biblioteca Scikit-learn para desenvolver e avaliar modelos de classificação.

### 2.6. Dashboard

Será desenvolvido um dashboard para apresentar os principais indicadores, padrões e resultados encontrados durante as análises.

As ferramentas de visualização serão avaliadas conforme as necessidades do projeto.

## 3. Tecnologias utilizadas e planejadas

**Já utilizadas:**
- Python;
- Pandas;
- SQLAlchemy;
- PyMySQL;
- python-dotenv;
- MySQL.

**Planejadas:**
- Docker;
- Apache Airflow;
- Scikit-learn;
- Power BI ou Streamlit.

## 4. Fluxo geral

Base original → Análise Exploratória Inicial → Extract → Transform → Validações → Load → Integração do Pipeline → Análise de Dados → Machine Learning → Dashboard.

## 5. Observações

O pipeline ETL possui as etapas de extração, transformação e carga implementadas e integradas pelo arquivo `main.py`, com execução completa testada com sucesso.

As validações iniciais de qualidade foram implementadas e aprovadas para a base utilizada no projeto.

As próximas melhorias serão voltadas ao aprimoramento do tratamento de erros e à ampliação das análises dos dados.

Docker e Apache Airflow serão incorporados em etapas futuras para containerização e orquestração do pipeline, respectivamente.

A implementação de uma área de quarentena para registros inválidos ficará reservada para uma etapa posterior do desenvolvimento.