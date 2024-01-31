drop database if exists students_db;
create database if not exists students_db;
use students_db;

drop table if exists student;
create table if not exists student
(
rno int unsigned unique,
name varchar(20) not null,
phone bigint(10) not null,
email varchar(30),
engg_year enum("fe","se","te","be"),
constraint uk1_email unique(email)
);

desc student;

alter table student add constraint uk2_phone unique(phone);
alter table student drop index uk1_email;

desc student;