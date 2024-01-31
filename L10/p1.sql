
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

-- aggregate function     return single summary values
-- count , max(),min(),sum(),avg()

-- wamq to find total students
select count(*) from student;


-- wamq to find students from thane
select count(*) from student where location = "thane";

-- wamq to find students from mumbai
select count(*) from student where location = "mumbai";

-- wamq to find total students location wise
select location , count(*) from student group by location;

-- wamq to find total students gender wise
select gender , count(*) from student group by gender;

-- wamq to find total students location, gender

select location,gender,count(*) from student group by location,gender;

select location,gender,count(*) from student group by location,gender 
order by location;

-- wamq to find max marks for male

select location,gender,count(*) from student group by location,gender 
having count(*)>= 2 order by location;

-- wamq to find max marks

select max(marks) from student;

-- wamq to find max marks for male

select max(marks) from student where gender ="male";

-- wamq to find max marks in mumbai

select max(marks) from student where location = "mumbai";

-- wamq to find min marks location wise 

select location,min(marks) from student group by location;

-- wamq to find sum of marks gender wise

select gender,sum(marks) from student group by gender;

-- wamq to find avg marks eyear wise

select eyear,avg(marks) from student group by eyear;

-- wamq to find max marks eyear wise , gender wise

select eyear,gender,max(marks) from student group by eyear,gender;

--  wamq to display students info who got highest marks

select * from student order by marks desc limit 1; 

select max(marks) from student;
select * from student where marks = 98;

select * from student where marks = ( select max(marks) from student );

select * from student where marks in ( select max(marks) from student );


-- wamq to display student who got the highest marks location wise
-- avoid this but this is correct 
select location,max(marks) from student group by location;
select * from student where location = "mumbai" and marks=98;
select * from student where location = "thane" and marks =93;

-- this is right but use in operator
select * from student where marks = (select max(marks) from student group by location);

select * from student where marks in (select max(marks) from student group by location);

select * from student where marks =ANY (select max(marks) from student group by location);

select * from student where marks =SOME (select max(marks) from student group by location);






















