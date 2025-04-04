import pandas as pd
import unicodedata

from code.database.DBCreateTable import DBCreateTable
from code.database.DBconfig import Dbconfig


class ANSDataProcessor(Dbconfig):
    def __init__(self, host: str, user: str, password: str, dbname: str):
        super().__init__(host, user, password, dbname)

    def create_table(self):
        conn = self.connect(self.host, self.user, self.password, self.dbname)

        cursor = conn.cursor()
        DBCreateTable.create_table(cursor)

        csv_file_relatorio = './code/database/Relatorio_cadop.csv'
        df = pd.read_csv(csv_file_relatorio, sep=';')

        # 🔄 Trocar qualquer valor que seja NaN (float), string "nan", "", etc por None
        df.replace(to_replace=["nan", "NaN", "NAN", "", "nan"], value=None, inplace=True)
        df = df.where(pd.notnull(df), None)

        for __, row in df.iterrows():
            row_dict = row.to_dict()  # criando um dicionario com cada linha ou array, assim ficando mais facil de alterar algo
            values = [None if pd.isna(val) else val for val in
                      row_dict.values()]  # verificando se um campo esta vazio, se estvier vai voltar none
            cursor.execute(
                """
                INSERT IGNORE INTO ans_operadoras (
                    Registro_ANS,CNPJ,Razao_Social,Nome_Fantasia,Modalidade,Logradouro,Numero,Complemento,
                    Bairro,Cidade,UF,CEP, DDD,Telefone,Fax,Endereco_eletronico,Representante,Cargo_Representante,
                    Regiao_de_Comercializacao,Data_Registro_ANS
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                values
            )
        conn.commit()

        for k in range(3,5):
            for i in range(1, 5):
                csv_file = f'./code/database/202{k}/' + str(i) + f'T202{k}/' + str(i) + f'T202{k}.csv'
                df = pd.read_csv(csv_file, sep=';')
                df['DESCRICAO'] = df['DESCRICAO'].apply(self.remover_acentos)
                df['DATA'] = pd.to_datetime(df['DATA'], dayfirst=True).dt.strftime('%Y-%m-%d')

                data_batch = []
                batch_size = 20000  # Tamanho do lote

                for __, row in df.iterrows():
                    row_dict = row.to_dict()
                    values = [None if pd.isna(val) else val for val in row_dict.values()]
                    data_batch.append(values)  # inserindo os valores

                    if len(data_batch) == batch_size:  # verifica se a quantidade de querys é igual a 20000 assim para executar o insert
                        cursor.executemany(
                            """
                            INSERT IGNORE INTO despesas_operadoras (
                                DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL
                            ) VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            data_batch
                        )
                        conn.commit()
                        data_batch = []  # limpa o lote

                # Inserção final para o que sobrou, caso nao tenha 1000 arquivos
                if data_batch:
                    cursor.executemany(
                        """
                        INSERT IGNORE INTO despesas_operadoras (
                            DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                        """,
                        data_batch
                    )
                    conn.commit()

        cursor.close()
        conn.close()


        print('Dados com sucesso!')

    def remover_acentos(self, texto):
        if pd.isna(texto):
            return texto
        return unicodedata.normalize('NFKD', str(texto)).encode('ASCII', 'ignore').decode('ASCII').strip()

