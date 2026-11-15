import pandas as pd
from pathlib import Path

def extract_data():
        raiz_projeto = Path(__file__).resolve().parent.parent

        caminho_arquivo = raiz_projeto / "data/raw/tech_employees.csv"

        dados = pd.read_csv(
                caminho_arquivo,
                sep=";",
                skiprows=2
        )
        return dados