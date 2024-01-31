-- this is soln to pract 4

drop database if exists kit_17dec22;
create database if not exists kit_17dec22;
use kit_17dec22;

create table if not exists dept(did int primary key,dname varchar(10));
insert into dept values (1,"Comps"),(2,"IT"),(3,"Elex");

create table if not exists student(rno int primary key,name varchar(20),did int,
foreign key(did) references dept(did) on delete set null);

insert into student values(10,"amit",1);
insert into student values(12,"vedant",2);
insert into student values(11,"sumit",3);

delete from dept where did=3;
select * from dept;
select * from student; 