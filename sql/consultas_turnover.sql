CREATE DATABASE db_turnover;
USE db_turnover;

SHOW DATABASES;

SELECT COUNT(*) AS total_funcionarios
FROM funcionarios;

SELECT *
FROM funcionarios
LIMIT 5;

DESCRIBE funcionarios;