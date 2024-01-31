/*wams to create a database and table*/

drop database if exists ved_s22;
create database if not exists ved_s22;
use ved_s22;
create table if not exists student
(
	rno tinyint unsigned primary key,
	dis varchar(1) not null,
	std tinyint
);

desc student;
select *  from student;
insert into student values(1,"A",5);
insert into student values(2,"B",6);
select *  from student;