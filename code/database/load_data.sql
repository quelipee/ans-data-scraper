LOAD DATA LOCAL INFILE './code/database/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;