
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data


def pipeline():
    """
    Executa o pipeline ETL completo:
    Extract → Transform → Load.
    """

    print("Iniciando pipeline ETL...")

    # 1. Extração
    dados = extract_data()
    print("Extração concluída!")

    # 2. Transformação
    dados = transform_data(dados)
    print("Transformação concluída!")

    # 3. Carga
    load_data(dados)
    print("Carga concluída!")

    print("Pipeline ETL finalizado com sucesso!")


if __name__ == "__main__":
    pipeline()
