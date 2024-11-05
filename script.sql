create database if not exists team_management;

use championship_management;

create table campeonato(
nome varchar(100),
modelo varchar(100),
premiacao varchar(100),
dt_termino date,
dt_inicio date,
id integer PRIMARY key
);

create table clube(
nome varchar(255),
id integer PRIMARY KEY,
dt_fundacao date,
titulos varchar(255)
);

create table jogador(
nome varchar(255),
cpf varchar(100) primary key,
posicao varchar(50),
numero integer,
tempo_contrato varchar(100),
titular boolean,
dt_nascimento date,
salario double
);

create table treinador(
dt_nascimento date,
salario double,	
nome varchar(255),
cpf varchar(100) primary key,
categoria varchar(50),
tempo_contrato varchar(100),
cargo varchar(30)
);

create table medico(
salario double,
nome varchar(255),
dt_nascimento date,
crm varchar(100) primary key,
especializacao varchar(50)
);

create table participa(
    campeonato_id integer,
    clube_id integer,
    primary key (campeonato_id, clube_id),
    foreign key (campeonato_id) references campeonato(id),
    foreign key (clube_id) references clube(id)
);

create table possui(
    clube_id integer,
    jogador_cpf varchar(100),
    primary key (clube_id, jogador_cpf),
    foreign key (clube_id) references clube(id),
    foreign key (jogador_cpf) references jogador(cpf)
);

create table comanda(
    clube_id integer,
    treinador_cpf varchar(100),
    primary key (clube_id, treinador_cpf),
    foreign key (clube_id) references clube(id),
    foreign key (treinador_cpf) references treinador(cpf)
);

create table emprega(
    clube_id integer,
    medico_crm varchar(100),
    primary key (clube_id, medico_crm),
    foreign key (clube_id) references clube(id),
    foreign key (medico_crm) references medico(crm)
);
