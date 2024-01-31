
drop database if exists tcs_27dec22;
create database if not exists tcs_27dec22;
use tcs_27dec22;

create table if not exists emp
(
id int unsigned primary key auto_increment,
name varchar(20) not null,
salary decimal(10,2) unsigned not null
);

desc emp;

insert into emp values ( 10, "amit", 4000);
insert into emp values ( default, "sumit", 5000);
insert into emp values ( default, "neha",4500);
select * from emp;
