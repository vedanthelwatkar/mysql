drop database if exists kit_28dec22;
create database if not exists kit_28dec22;
use kit_28dec22;

create table if not exists student
(
rno int unsigned primary key,
name varchar(20),
marks tinyint unsigned,
eyear enum ("fe","se","te","be"),
location varchar(30) default "mumbai"
);
desc student;

insert into student values (10,"amit",98,"fe","thane");
insert into student values (20,"sumit",79,"se","mumbai");
insert into student values (30,"rumit",63,"fe","thane");
insert into student values (40,"seema",81,"se","thane");
insert into student values (50,"reema",45,"fe","mumbai");
insert into student values (60,"tina",95,"be","thane");

select  * from student;
