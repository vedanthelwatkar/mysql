-- this is pract 2

use kc_24dec22;

drop table if exists student;
create table if not exists student
(
id int unsigned primary key,
name varchar(20) not null,
ptr double not null,
location varchar(20) not null default "thane",
gender enum("m","f"),
branch varchar(10) not null,
cid int unsigned,
foreign key (cid) references courses (cid)
);

desc student;
desc courses;

insert into student values(10,"amit",7.6,"thane","m","comp",2);
insert into student values(20,"neha",9.2,"mumbai","f","extc",1);
insert into student values(30,"sumit",8.2,"thane",default,"comp",2);
insert into student values(40,"reena",5.5,"thane","f","it",3);

select * from student;
