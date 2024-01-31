-- P5

drop database if exists tcs_2jan23;
create database if not exists tcs_2jan23;
use tcs_2jan23;

create table if not exists emp
(
id int unsigned primary key auto_increment,
name varchar(50) not null,
salary decimal(10,2) unsigned not null,
location varchar(50) default "mumbai",
dept varchar(40)
);
desc emp;

insert into emp values(default,"amit",5000,default,"sales");
insert into emp values(default,"neha",3000,"pune","sales");
insert into emp values(default,"sumit",4000,default,"finance");
insert into emp values(default,"raj",5000,"pune","finance");
insert into emp values(default,"pooja",6000,default,"sales");

select * from emp;