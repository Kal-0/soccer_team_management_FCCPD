CREATE DATABASE IF NOT EXISTS team_management;

USE team_management;

CREATE TABLE campeonatos (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    modelo VARCHAR(100),
    premiacao VARCHAR(100),
    dt_termino DATE,
    dt_inicio DATE
);

CREATE TABLE clubes (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    dt_fundacao DATE,
    titulos VARCHAR(255)
);

CREATE TABLE jogadores (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    cpf VARCHAR(100) UNIQUE,  -- Tornou o CPF único
    nome VARCHAR(255),
    posicao VARCHAR(50),
    numero INTEGER,
    tempo_contrato VARCHAR(100),
    titular BOOLEAN,
    dt_nascimento DATE,
    salario DOUBLE
);

CREATE TABLE treinadores (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    cpf VARCHAR(100) UNIQUE,  -- Tornou o CPF único
    nome VARCHAR(255),
    categoria VARCHAR(50),
    tempo_contrato VARCHAR(100),
    cargo VARCHAR(30),
    dt_nascimento DATE,
    salario DOUBLE
);

CREATE TABLE medicos (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    crm VARCHAR(100) UNIQUE,  -- Tornou o CRM único
    nome VARCHAR(255),
    especializacao VARCHAR(50),
    dt_nascimento DATE,
    salario DOUBLE
);

CREATE TABLE campeonato_clube (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    campeonato_id INTEGER,
    clube_id INTEGER,
    FOREIGN KEY (campeonato_id) REFERENCES campeonatos(id),
    FOREIGN KEY (clube_id) REFERENCES clubes(id)
);

CREATE TABLE clube_jogador (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    clube_id INTEGER,
    jogador_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id),
    FOREIGN KEY (jogador_id) REFERENCES jogadores(id)
);

CREATE TABLE clube_treinador (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    clube_id INTEGER,
    treinador_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id),
    FOREIGN KEY (treinador_id) REFERENCES treinadores(id)
);

CREATE TABLE clube_medico (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    clube_id INTEGER,
    medico_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id),
    FOREIGN KEY (medico_id) REFERENCES medicos(id)
);
