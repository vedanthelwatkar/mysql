-- this is pract 1
drop database if exists kc_26dec22;
create database if not exists kc_26dec22;
use kc_26dec22;

create table if not exists student
(
rno int unsigned primary key auto_increment,
name varchar(20) not null,
gender enum ("m","f"),
location varchar(20) default "mumbai",
marks tinyint unsigned,
eyear enum ("fe","se","te","be") not null,
acard varchar(15) not null
);

desc student;


insert into student values(default,"amit","m",default,78,"fe","123");
insert into student values(default,"neha","f","thane",65,"se","223");
insert into student values(default,"sumit","m","thane",92,"se","153");
insert into student values(default,"tina","f",default,28,"fe","163");

select * from student;

create or replace view v1 as select rno,name from student;
select * from v1;

create or replace view v2 as select rno as rollnumber,name as stu_name from student;
select * from v2;

create or replace view v3(rollnumber,sname) as select rno,name from student;
select * from v3;

create or replace view v4 as select * from student where eyear="fe";
select * from v4;

create or replace view v5 as select * from student where eyear="se";
select * from v5;

create or replace view v6 as
select * from student order by marks desc limit 1;
select * from v6;

create or replace view v7 as
select * from student where marks in (select max(marks) from student);
select * from v7;










