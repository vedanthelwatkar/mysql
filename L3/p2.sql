drop database if exists kc_14dec22;
create database if not exists kc_14dec22;
use kc_14dec22;
create table if not exists student
(
	rno int unsigned primary key,
	name varchar(20) not null,
	marks tinyint unsigned
);
desc student;
select * from student;
insert into student values (10,"neha",95);
insert into student values (2,"suraj",67);
select * from student;