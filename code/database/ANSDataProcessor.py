import pandas as pd
import mysql.connector
from code.database.DBconfig import Dbconfig


class ANSDataProcessor(Dbconfig):
    def __init__(self, db_config, host: str, user: str, password: str, dbname: str):
        super().__init__(host, user, password, dbname)

    def create_table(self):
        conn = self.connect(self.host, self.user, self.password,self.dbname)

        cursor = conn.cursor()
        ANSDataProcessor.create_table_operadoras(cursor)

        csv_file_relatorio = './code/database/Relatorio_cadop.csv'
        df = pd.read_csv(csv_file_relatorio, sep=';')

        # 🔄 Trocar qualquer valor que seja NaN (float), string "nan", "", etc por None
        df.replace(to_replace=["nan", "NaN", "NAN", "", "nan"], value=None, inplace=True)
        df = df.where(pd.notnull(df), None)

        for __, row in df.iterrows():
            row_dict = row.to_dict() # criando um dicionario com cada linha ou array, assim ficando mais facil de alterar algo
            values = [None if pd.isna(val) else val for val in row_dict.values()] # verificando se um campo esta vazio, se estvier vai voltar none
            cursor.execute(
                """
                INSERT INTO ans_operadoras (
                    Registro_ANS,
                    CNPJ,
                    Razao_Social,
                    Nome_Fantasia,
                    Modalidade,
                    Logradouro,
                    Numero,
                    Complemento,
                    Bairro,
                    Cidade,
                    UF,
                    CEP,
                    DDD,
                    Telefone,
                    Fax,
                    Endereco_eletronico,
                    Representante,
                    Cargo_Representante,
                    Regiao_de_Comercializacao,
                    Data_Registro_ANS
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                values
            )
        conn.commit()
        cursor.close()
        conn.close()

        print('Dados com sucesso!')

        # for i in range(1, 5):
        #     csv_file = './code/database/2023/' + str(i) + 'T2023'
        #     df = pd.read_csv(csv_file)

    @staticmethod
    def create_table_operadoras(cursor):
        tabela_sql = """
                CREATE TABLE IF NOT EXISTS ans_operadoras (
                Registro_ANS INT PRIMARY KEY,
                CNPJ VARCHAR(14) NOT NULL,
                Razao_Social VARCHAR(255) NOT NULL,
                Nome_Fantasia VARCHAR(255),
                Modalidade VARCHAR(100),
                Logradouro VARCHAR(255),
                Numero VARCHAR(20),
                Complemento VARCHAR(100),
                Bairro VARCHAR(100),
                Cidade VARCHAR(100),
                UF CHAR(2),
                CEP VARCHAR(8),
                DDD CHAR(32),
                Telefone VARCHAR(20),
                Fax VARCHAR(20),
                Endereco_eletronico VARCHAR(255),
                Representante VARCHAR(255),
                Cargo_Representante VARCHAR(100),
                Regiao_de_Comercializacao INT,
                Data_Registro_ANS DATE
                )"""

        tabela_sql_despesas = """
                CREATE TABLE IF NOT EXISTS despesas_operadoras (
                id INT AUTO_INCREMENT PRIMARY KEY,
                DATA DATE NOT NULL,
                REG_ANS INT NOT NULL,
                CD_CONTA_CONTABIL VARCHAR(10) NOT NULL,
                DESCRICAO VARCHAR(255) NOT NULL,
                VL_SALDO_INICIAL DECIMAL(15,2),
                VL_SALDO_FINAL DECIMAL(15,2),
                FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
            )"""
        cursor.execute(tabela_sql)
        cursor.execute(tabela_sql_despesas)

