--  this is  a story of KC


drop database if exists kc_22dec22;
create database if not exists kc_22dec22;
use kc_22dec22;

create table if not exists dept
(
did int unsigned primary key,
dname varchar(20)
);

insert into dept values (1,"finance");
insert into dept values(2,"sales");

select * from dept;

create table if not exists emp
(
eid int unsigned primary key,
ename varchar(20) not null,
reports_to int unsigned,
did int unsigned,
foreign key(did) references dept (did)
);

desc emp;

insert into emp values(100,"kamal",Null,1);
insert into emp values(200,"vishal",100,1);
insert into emp values(300,"amit",100,2);
insert into emp values(400,"sumit",200,1);
insert into emp values(500,"neha",300,2);

select * from dept;
select * from emp;









