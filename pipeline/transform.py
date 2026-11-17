import pandas as pd

def transform_data(dados):

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

    dados = pd.get_dummies(
        dados,
        columns=["Estado_Civil"],
        dtype=int
    )

    dados = pd.get_dummies(
        dados,
        columns=["Frequência de Viagens"],
        dtype=int
    )

    dados = pd.get_dummies(
        dados,
        columns=["Formação"],
        dtype=int
    )

    dados["E-Sat"] = dados["E-Sat"].map({
    "Baixo": 1,
    "Médio": 2,
    "Alto": 3,
    "Muito Alto": 4
    })

    dados["Gênero"] = dados["Gênero"].map({
    "H": 0,
    "M":1
    })

    dados["Equilibrio_de_Vida"] = dados["Equilibrio_de_Vida"].map({
        "Ruim": 1,
        "Bom": 2,
        "Muito bom": 3,
        "Excelente": 4
    })


    return dados