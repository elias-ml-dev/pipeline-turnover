import pandas as pd

def transform_data(dados):
    dados.info()

    dados["Funcionário_deixou_a_empresa"] = dados[
        "Funcionário_deixou_a_empresa"
        ].replace({
        "Sim": 1,
        "Não": 0
    }).infer_objects(copy=False)

    dados["Faz_hora_extras?"] = dados[
        "Faz_hora_extras?"
        ].replace({
            "Sim": 1,
            "Não": 0
        }).infer_objects(copy=False)

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
    
    return dados