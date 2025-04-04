from code.database.DBconfig import Dbconfig


class QueryTopOperators(Dbconfig):
    def __init__(self, host: str, user: str, password: str, dbname: str):
        super().__init__(host, user, password, dbname)
        self.conn = self.connect(host=self.host, user=self.user, password=self.password, dbname=self.dbname)
        self.cursor = self.conn.cursor()

    def get_top_10_expenses_last_quarter(self):
        query = f"""
                    SELECT
                        ao.Razao_Social,
                        ao.Nome_Fantasia,
                        do.REG_ANS,
                        COALESCE(SUM(do.VL_SALDO_FINAL), 0) AS total_despesa
                    FROM despesas_operadoras do
                    INNER JOIN ans_operadoras ao ON do.REG_ANS = ao.Registro_ANS
                    WHERE do.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR' -- Evita erro se houver pequenas variações
                      AND do.DATA >= (
                          SELECT DATE_SUB(MAX(DATA), INTERVAL 3 MONTH)
                          FROM despesas_operadoras
                      )
                    GROUP BY do.REG_ANS, ao.Razao_Social, ao.Nome_Fantasia
                    ORDER BY total_despesa DESC
                    LIMIT 10;
            """

        self.cursor.execute(query)
        # print(cursor.fetchall())
        for row in self.cursor.fetchall():
            razao_social = row[0]
            nome_fantasia = row[1]
            reg_ans = row[2]
            total_despesa = row[3]

            print(f"""
            Razão Social   : {razao_social}
            Nome Fantasia  : {nome_fantasia}
            REG ANS        : {reg_ans}
            Total Despesa  : R$ {total_despesa:,.2f}
            """)
        self.cursor.close()
        self.conn.close()

    def get_top_10_expenses_last_year(self):
        query_year = f"""
                    SELECT
                        ao.Razao_Social,
                        ao.Nome_Fantasia,
                        do.REG_ANS,
                        COALESCE(SUM(do.VL_SALDO_FINAL), 0) AS total_despesa
                    FROM despesas_operadoras do
                    INNER JOIN ans_operadoras ao ON do.REG_ANS = ao.Registro_ANS
                    WHERE do.DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR'
                      AND do.DATA >= (
                          SELECT DATE_SUB(MAX(DATA), INTERVAL 12 MONTH)
                          FROM despesas_operadoras
                      )
                    GROUP BY do.REG_ANS, ao.Razao_Social, ao.Nome_Fantasia
                    ORDER BY total_despesa DESC
                    LIMIT 10;
        """

        self.cursor.execute(query_year)
        for row in self.cursor.fetchall():
            razao_social = row[0]
            nome_fantasia = row[1]
            reg_ans = row[2]
            total_despesa = row[3]

            print(f"""
            Razão Social   : {razao_social}
            Nome Fantasia  : {nome_fantasia}
            REG ANS        : {reg_ans}
            Total Despesa  : R$ {total_despesa:,.2f}
            """)
        self.cursor.close()
        self.conn.close()