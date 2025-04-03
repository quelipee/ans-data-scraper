SET FOREIGN_KEY_CHECKS = 0;
LOAD DATA INFILE '/var/lib/mysql-files/3T2024.csv'
INTO TABLE despesas_operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cd_conta_contabil, @descricao, @vl_saldo_inicial, @vl_saldo_final)
SET
    DATA = STR_TO_DATE(NULLIF(@data, ''), '%Y-%m-%d'),
    REG_ANS = NULLIF(TRIM(@reg_ans), ''),
    CD_CONTA_CONTABIL = @cd_conta_contabil,
    DESCRICAO = @descricao,
    VL_SALDO_INICIAL = REPLACE(NULLIF(@vl_saldo_inicial, ''), ',', '.'),
    VL_SALDO_FINAL = REPLACE(NULLIF(@vl_saldo_final, ''), ',', '.');
SET FOREIGN_KEY_CHECKS = 1;