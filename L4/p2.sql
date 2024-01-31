-- this is solution to practical 2

drop database if exists bike_db;
create database if not exists bike_db;
use bike_db;
create table if not exists bike
(
	id int unsigned primary key ,
	model_name varchar(20),
	color enum("red","blue","black","white") default "black",
	options set("light","helmet","lock")
);
desc bike;

insert into bike values(100,"maruti","red","light");
insert into bike values(110,"suzuki","blue","helmet");
insert into bike values(120,"honda",default,null);
insert into bike values(130,"mercedes",default,"lock");
insert into bike values(140,"bmw",default,null);
select * from bike;