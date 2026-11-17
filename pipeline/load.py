import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine

raiz_projeto = Path(__file__).resolve().parent.parent

load_dotenv(raiz_projeto / ".env")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as conexao:
            print("Conexão com MySQL realizada com sucesso!")

    except Exception as erro:
        print(f"Erro ao conectar com MySQL: {erro}")


def load_data(dados):
    raiz_projeto = Path(__file__).resolve().parent.parent
    caminho_arquivo = raiz_projeto /"data"/"processed"/"tech_employees_processed.csv"

    try:
        dados.to_csv(
            caminho_arquivo,
            index=False,
            sep=";"
        )
        dados.to_sql(
            name="funcionarios",
            con=engine,
            if_exists="replace",
            index=False
        )

    except Exception as erro:
        print(f"Erro ao realizar a carga: {erro}")

    else:
        print("Carga CSV e MySQL concluída com sucesso!")