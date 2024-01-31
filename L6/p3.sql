-- this is pract 3

drop database if exists kit_17dec22;
create database if not exists kit_17dec22;
use kit_17dec22;

create table if not exists dept(did int,name varchar(20));
insert into dept values(1,"Comps"),(2,"IT),(3,"Elex");

create table if not exists student
(rno int primary key,name varchar(20),did int,
foreign key(did) references dept(did));

insert into student values(10,"nikita",1);
insert into student values(11,"rikita",2);
insert into student values(12,"sangita",3);

select * from dept;
select * from student;