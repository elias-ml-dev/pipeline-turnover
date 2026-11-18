
import pandas as pd

def transform_data(dados):

    # Data Mapping: convertendo Sim e Não para valores numéricos (1 e 0)
    dados["Funcionário_deixou_a_empresa"] = dados[
        "Funcionário_deixou_a_empresa"
    ].map({
        "Sim": 1,
        "Não": 0
    })

    dados["Faz_hora_extras?"] = dados[
        "Faz_hora_extras?"
    ].map({
        "Sim": 1,
        "Não": 0
    })

    # One-Hot Encoding: separando as categorias de estado civil em colunas
    dados = pd.get_dummies(
        dados,
        columns=["Estado_Civil"],
        dtype=int
    )

    # One-Hot Encoding: separando as categorias de frequência de viagens
    dados = pd.get_dummies(
        dados,
        columns=["Frequência de Viagens"],
        dtype=int
    )

    # One-Hot Encoding: separando os níveis de formação em colunas
    dados = pd.get_dummies(
        dados,
        columns=["Formação"],
        dtype=int
    )

    # Ordinal Encoding: convertendo os níveis de satisfação em valores numéricos
    dados["E-Sat"] = dados["E-Sat"].map({
        "Baixo": 1,
        "Médio": 2,
        "Alto": 3,
        "Muito Alto": 4
    })

    # Data Mapping: convertendo gênero para valores numéricos
    dados["Gênero"] = dados["Gênero"].map({
        "H": 0,
        "M": 1
    })

    # Ordinal Encoding: convertendo o equilíbrio de vida em valores numéricos
    dados["Equilibrio_de_Vida"] = dados["Equilibrio_de_Vida"].map({
        "Ruim": 1,
        "Bom": 2,
        "Muito bom": 3,
        "Excelente": 4
    })

    # Data Validation: verificando se todos os IDs são únicos
    if not dados["ID"].is_unique:
        raise ValueError("Erro: existem IDs duplicados na base de dados!")

    print("Validação de IDs: aprovada. Todos os IDs são únicos.")

    # Data Validation: verificando se existem valores nulos
    if dados.isnull().any().any():
        raise ValueError("Erro: existem valores nulos na base de dados!")

    print("Validação de valores nulos: aprovada. Nenhum valor nulo encontrado.")

    # Duplicate Check: verificando se existem linhas duplicadas
    if dados.duplicated().any():
        raise ValueError("Erro: existem linhas duplicadas na base de dados!")

    print("Validação de duplicados: aprovada. Nenhuma linha duplicada encontrada.")

    # Data Integrity: verificando se a variável de saída possui apenas 0 e 1
    if not dados["Funcionário_deixou_a_empresa"].isin([0, 1]).all():
        raise ValueError("Erro: foram encontrados valores inválidos na variável de saída!")

    print("Data Integrity: aprovada. A coluna 'Funcionário_deixou_a_empresa' contém apenas 0 e 1.")

    # Range Check: verificando se as idades estão dentro da faixa permitida
    if not dados["Idade"].between(18, 60).all():
        raise ValueError("Erro: foram encontradas idades fora da faixa permitida!")

    print("Range Check: aprovado. Todas as idades estão dentro da faixa permitida.")

    # Data Integrity: verificando se os salários são maiores que zero
    if not (dados["Salário"] > 0).all():
        raise ValueError("Erro: foram encontrados salários zerados ou negativos!")

    print("Salary Check: aprovado. Todos os salários são maiores que zero.")

    # Range Check: verificando se a quantidade de empresas trabalhadas não é negativa
    if not (dados["Qte_Empresas_Trabalhadas"] >= 0).all():
        raise ValueError("Erro: foram encontrados valores negativos na quantidade de empresas trabalhadas!")

    print("Range Check: aprovado. Nenhum valor negativo encontrado na quantidade de empresas trabalhadas.")

    # Range Check: verificando se o tempo de empresa não é negativo
    if not (dados["Tempo_de_empresa"] >= 0).all():
        raise ValueError("Erro: foram encontrados valores negativos no tempo de empresa!")

    print("Range Check: aprovado. Nenhum valor negativo encontrado no tempo de empresa.")


    # Range Check: verificando se os anos no mesmo cargo não são negativos
    if not (dados["Anos_no_mesmo_cargo"] >= 0).all():
        raise ValueError("Erro: foram encontrados valores negativos nos anos no mesmo cargo!")

    print("Range Check: aprovado. Nenhum valor negativo encontrado nos anos no mesmo cargo.")

    # Range Check: verificando se os anos desde a última promoção não são negativos
    if not (dados["Anos_desde_a_ultima_promocao"] >= 0).all():
        raise ValueError("Erro: foram encontrados valores negativos nos anos desde a última promoção!")

    print("Range Check: aprovado. Nenhum valor negativo encontrado nos anos desde a última promoção.")

    # Range Check: verificando se os anos com o mesmo chefe não são negativos
    if not (dados["Anos_com_o_mesmo_chefe"] >= 0).all():
        raise ValueError("Erro: foram encontrados valores negativos nos anos com o mesmo chefe!")

    print("Range Check: aprovado. Nenhum valor negativo encontrado nos anos com o mesmo chefe.")

    return dados
