-- this is solution to practical 1

drop database if exists ticket_db;
create database if not exists ticket_db;
use ticket_db;
create table ticket(id int , title varchar(225) not null, priority enum("low","medium","high"));
desc ticket;

insert into ticket values(100,"food quality is good","high");
insert into ticket values(110,"food quality is bad","low");
select * from ticket;
	
