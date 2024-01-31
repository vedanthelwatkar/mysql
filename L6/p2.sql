-- this is soln to pract 2

drop database if exists employee_db;
create database if not exists employee_db;
use employee_db;

drop table if exists employee;
create table if not exists employee
(
eid int unsigned,
ename varchar(30),
esalary decimal(10,2),
primary key(eid,ename)
);

desc employee;

alter table employee drop primary key;
desc employee;
alter table employee add constraint cab primary key(eid);
desc employee;
