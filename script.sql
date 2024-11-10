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
    salario DOUBLE,
    clube_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id)
);

CREATE TABLE treinadores (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    cpf VARCHAR(100) UNIQUE,  -- Tornou o CPF único
    nome VARCHAR(255),
    categoria VARCHAR(50),
    tempo_contrato VARCHAR(100),
    cargo VARCHAR(30),
    dt_nascimento DATE,
    salario DOUBLE,
    clube_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id)
);

CREATE TABLE medicos (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    crm VARCHAR(100) UNIQUE,  -- Tornou o CRM único
    nome VARCHAR(255),
    especializacao VARCHAR(50),
    dt_nascimento DATE,
    salario DOUBLE,
    clube_id INTEGER,
    FOREIGN KEY (clube_id) REFERENCES clubes(id)
);

CREATE TABLE campeonato_clube (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,  -- Agora tem id como chave primária
    campeonato_id INTEGER,
    clube_id INTEGER,
    FOREIGN KEY (campeonato_id) REFERENCES campeonatos(id),
    FOREIGN KEY (clube_id) REFERENCES clubes(id)
);


-- Populando a tabela campeonatos
INSERT INTO campeonatos (nome, modelo, premiacao, dt_termino, dt_inicio) VALUES
('Campeonato Brasileiro', 'Pontos corridos', 'R$ 10.000.000', '2024-12-05', '2024-05-01'),
('Copa do Brasil', 'Eliminatória', 'R$ 3.000.000', '2024-11-30', '2024-03-10'),
('Libertadores', 'Grupos e eliminação', 'R$ 15.000.000', '2024-11-15', '2024-02-20'),
('Copa Sul-Americana', 'Eliminatória', 'R$ 4.500.000', '2024-11-28', '2024-03-15'),
('Copa do Mundo', 'Fase de grupos e eliminatória', 'US$ 50.000.000', '2024-12-15', '2024-06-01'),
('Supercopa', 'Eliminatória', 'R$ 1.500.000', '2024-10-01', '2024-09-01');

-- Populando a tabela clubes (times nordestinos e Rosenborg)
INSERT INTO clubes (nome, dt_fundacao, titulos) VALUES
('Sport Club do Recife', '1905-05-13', '1 Campeonato Brasileiro Série A, 1 Copa do Brasil, 3 Copa do Nordesete'),
('Bahia', '1931-01-01', '2 Campeonatos Brasileiros, 4 Copas do Nordeste'),
('Ceara Sporting Club', '1914-06-02', ' 2 Copas do Nordeste, 1 Campeonato Brasileiro Série B'),
('Fortaleza', '1918-10-18', '2 Copas do Nordeste, 1 Campeonato Brasileiro Série B'),
('Vitoria', '1899-05-13', '1 Campeonato Brasileiro Série B'),
('Rosenborg BK', '1917-05-19', '26 Norweigian Eliteserien titles, 12 Norwegian Cups');

-- Populando a tabela jogadores com novos jogadores
INSERT INTO jogadores (cpf, nome, posicao, numero, tempo_contrato, titular, dt_nascimento, salario, clube_id) VALUES
('12345678901', 'Cristiano Ronaldo', 'Atacante', 8, '3 anos', true, '1991-07-05', 800000, 1),
('56789012341', 'Lionel Messe', 'Ponta direita', 44, '4 anos', true, '1987-09-21', 950000, 1),
('23456789012', 'Anderson Pedra', 'Meio-campo', 17, '2 anos', true, '1995-11-24', 400000, 2),
('23286509012', 'Michael Jordan', 'Goleiro', 23, '2 anos', true, '1995-10-14', 400000, 2),
('34567890123', 'Ricardinho', 'Meio-campo', 20, '1 ano', false, '1987-01-06', 350000, 3),
('86564196123', 'Kobe Bryant', 'Lateral direito', 24, '1 ano', false, '1997-01-06', 350000, 3),
('45678901234', 'Vinicius Souza', 'Volante', 15, '5 anos', true, '1997-02-14', 600000, 4),
('45658109234', 'Diogo Henrique', 'Lateral esquerdo', 69, '5 anos', true, '2004-09-12', 600000, 4),
('51740012345', 'Rudiger', 'Zagueiro', 3, '4 anos', true, '1992-09-21', 550000, 5),
('56789012345', 'Mason Mount', 'Meio-campo', 3, '4 anos', true, '1982-04-11', 550000, 5),
('67890123456', 'Carlos Eduardo', 'Atacante', 11, '2 anos', false, '1996-01-18', 450000, 6),
('65891123456', 'Ronaldo', 'Zagueiro', 11, '2 anos', false, '1991-11-15', 450000, 6);

-- Populando a tabela treinadores com novos técnicos
INSERT INTO treinadores (cpf, nome, categoria, tempo_contrato, cargo, dt_nascimento, salario, clube_id) VALUES
('78901234567', 'Pep Guardiola', 'A', '2 anos', 'Treinador principal', '1963-01-10', 1200000, 1),
('89012345678', 'Roger Machado', 'A', '1 ano', 'Treinador principal', '1975-02-16', 1000000, 2),
('90123456789', 'Jorge Sampaoli', 'A', '2 anos', 'Treinador principal', '1960-03-11', 1800000, 3),
('01234567890', 'Vagner Mancini', 'B', '1 ano', 'Treinador assistente', '1961-09-24', 800000, 4),
('12345678901', 'Enderson Moreira', 'A', '2 anos', 'Treinador principal', '1971-11-05', 1500000, 5),
('23456789012', 'Erik Hamrén', 'A', '1 ano', 'Treinador principal', '1957-06-27', 2000000, 6);


-- Populando a tabela medicos
INSERT INTO medicos (crm, nome, especializacao, dt_nascimento, salario, clube_id) VALUES
('1234567890', 'Dr. Ricardo', 'Ortopedia', '1980-06-10', 300000, 1),
('2345678901', 'Dr. João', 'Cardiologia', '1975-11-15', 350000, 2),
('3456789012', 'Dr. Lucas', 'Neurologia', '1982-03-22', 280000, 3),
('4567890123', 'Dr. Rafael', 'Fisioterapia', '1988-07-30', 220000, 4),
('5678901234', 'Dra. Ana', 'Psicologia', '1990-01-17', 250000, 5),
('6789012345', 'Dr. Marcos', 'Ginecologia', '1985-04-12', 270000, 6);

-- Populando a tabela campeonato_clube
INSERT INTO campeonato_clube (campeonato_id, clube_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 6),
(3, 1),
(3, 2),
(3, 3),
(4, 4),
(4, 5),
(4, 6),
(5, 1),
(5, 2),
(5, 3),
(6, 4),
(6, 5),
(6, 6);
