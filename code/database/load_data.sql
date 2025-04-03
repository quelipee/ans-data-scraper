LOAD DATA INFILE '/var/lib/mysql-files/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Registro_ANS, @CNPJ, @Razao_Social, @Nome_Fantasia, @Modalidade, @Logradouro,
 @Numero, @Complemento, @Bairro, @Cidade, @UF, @CEP, @DDD, @Telefone, @Fax,
 @Endereco_eletronico, @Representante, @Cargo_Representante,
 @Regiao_de_Comercializacao, @Data_Registro_ANS)
SET
    Registro_ANS = NULLIF(@Registro_ANS, ''),
    CNPJ = NULLIF(@CNPJ, ''),
    Razao_Social = NULLIF(@Razao_Social, ''),
    Nome_Fantasia = NULLIF(@Nome_Fantasia, ''),
    Modalidade = NULLIF(@Modalidade, ''),
    Logradouro = NULLIF(@Logradouro, ''),
    Numero = NULLIF(@Numero, ''),
    Complemento = NULLIF(@Complemento, ''),
    Bairro = NULLIF(@Bairro, ''),
    Cidade = NULLIF(@Cidade, ''),
    UF = NULLIF(@UF, ''),
    CEP = NULLIF(@CEP, ''),
    DDD = NULLIF(@DDD, ''),
    Telefone = NULLIF(@Telefone, ''),
    Fax = NULLIF(@Fax, ''),
    Endereco_eletronico = NULLIF(@Endereco_eletronico, ''),
    Representante = NULLIF(@Representante, ''),
    Cargo_Representante = NULLIF(@Cargo_Representante, ''),
    Regiao_de_Comercializacao = NULLIF(@Regiao_de_Comercializacao, ''),
    Data_Registro_ANS = STR_TO_DATE(NULLIF(@Data_Registro_ANS, ''), '%Y-%m-%d');

