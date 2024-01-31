-- this is DML demo

drop database if exists kc_20dec22;
create database if not exists kc_20dec22;
use kc_20dec22;

create table if not exists student
(
rno int unsigned primary key auto_increment,
name varchar(10) not null,
marks tinyint unsigned,
gender enum("m", "f") not null,
location varchar(20) default "mumbai",
eyear enum("fe","se","te","be")
);

desc student;

insert into student values(default,"amit",98,"m",default,"fe");
insert student values(default,"seema",93,"f","thane","fe");
insert student value(default,"shyam",89,"m","mumbai","fe");
insert into student values(default,"sumit",76,"m","thane","fe");
insert into student values(default,"sneha",63,"f","thane","fe");
insert into student values(default,"neha",29,"f","mumbai","se");
insert into student(name,marks,gender,eyear) values("raj",88,"m","fe");
insert into student(name,gender,marks,eyear) values("raja","m",62,"se");
insert into student(name,gender,marks,eyear) values
("ram","m",65,"fe"),("sita","f",55,"fe");
insert into student set name="kiran",gender="m",marks="97",eyear="fe";
select * from student;

update student set marks = marks -10;
update student set marks = marks +2 where location ="thane";
select * from student;
update student set marks = marks + 1 where eyear = "fe";
select * from student;
update student set marks = marks -5 order by marks desc limit 1;
select * from student;
update student set marks = marks +10 order by marks limit 2;
select * from student;
delete from student where rno = 8;
select * from student;
delete from student order by marks limit 2;
select * from student;
