CREATE DATABASE ans_operadoras;
USE ans_operadoras;

CREATE TABLE operadoras (
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
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao INT NULL,
    Data_Registro_ANS DATE
);

CREATE TABLE despesas_operadoras(
    id INT AUTO_INCREMENT PRIMARY KEY,
    DATA DATE NOT NULL,
    REG_ANS INT NOT NULL,
    CD_CONTA_CONTABIL VARCHAR(10) NOT NULL,
    DESCRICAO VARCHAR(255) NOT NULL,
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
)


