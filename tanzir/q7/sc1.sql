CREATE DATABASE IF NOT EXISTS myDB;
USE myDB;

DROP TABLE IF EXISTS test;


CREATE TABLE IF NOT EXISTS test (
  id serial NOT NULL PRIMARY KEY,
  name varchar(100),
  lastname varchar(200),
  email varchar(200),
  modified timestamp default CURRENT_TIMESTAMP NOT NULL,
  INDEX `modified_index` (`modified`)
);
USE myDB;
INSERT INTO test (name, lastname, email) VALUES ('alice', 'alice@abc.com', 'eng.');
INSERT INTO test (name, lastname, email) VALUES ('bob1', 'bob1@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob2', 'bob2@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob3', 'bob3@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob4', 'bob4@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob5', 'bob5@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob6', 'bob6@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob7', 'bob7@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob8', 'bob8@abc.com', 'sales');
INSERT INTO test (name, lastname, email) VALUES ('bob9', 'bob9@abc.com', 'sales');

