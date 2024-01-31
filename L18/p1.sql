-- create database, create table, columns and records

drop database if exists kc_3jan23;
create database if not exists kc_3jan23;
use kc_3jan23; 

create table emp like tcs_2jan23.emp;
desc emp;
select * from emp;

insert into emp select * from tcs_2jan23.emp;
select * from emp;