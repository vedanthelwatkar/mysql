/*wams to create databse and table*/

drop database if exists ab_c12;
create database if not exists ab_c12;
use ab_c12;
create table if not exists wow
(
	name varchar(20) primary key,
	langu varchar(10),
	age tinyint unsigned
);

desc wow;
select * from wow;
insert into wow values("vedant","marathi",19);
insert into wow values("pramod","gujrati",49);
insert into wow values("priya","malyalum",44);
select * from wow;