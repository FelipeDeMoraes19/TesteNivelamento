DROP TABLE IF EXISTS operadoras_ativas CASCADE;
CREATE TABLE operadoras_ativas (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(20),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(255),
    representante VARCHAR(100),
    cargo_representante VARCHAR(100),
    regiao_comercializacao INTEGER,
    data_registro DATE
);

DROP TABLE IF EXISTS demonstracoes_contabeis;
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE,
    registro_ans VARCHAR(20),
    codigo_conta VARCHAR(50),
    descricao VARCHAR(255),
    saldo_inicial TEXT,
    saldo_final TEXT
);
