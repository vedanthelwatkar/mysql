drop database if exists kc_6jan23;
create database if not exists kc_6jan23;
use kc_6jan23;


create table if not exists student
(
rno int unsigned primary key,
name varchar(50) not null,
marks tinyint unsigned not null,
email varchar(100) unique not null
);

desc student;

delimiter $$
drop trigger if exists t1 $$
create trigger t1 before insert on student for each row
begin
	if (new.rno is null) or (new.rno < 1) then
		signal SQLSTATE '11111' set message_text = "invalid rno";
	end if;
	
	if (new.name is null) or (length(trim(new.name)) = 0) or (length(new.name) < 2) or
		(not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "invalid name";
	end if;

	if (new.marks is null) or (new.marks < 0) or (new.marks > 100) then
		signal SQLSTATE '33333' set message_text = "invalid marks";
	end if;
		
	if (new.email is null) or (length(trim(new.email)) = 0) then
		signal SQLSTATE '44444' set message_text = "invalid email";
	end if;  
end $$

drop trigger if exists t2 $$
create trigger t2 before update on student for each row
begin
	if (new.rno is null) or (new.rno < 1) then
		signal SQLSTATE '11111' set message_text = "invalid rno";
	end if;
	
	if (new.name is null) or (length(trim(new.name)) = 0) or (length(new.name) < 2) or 
		(not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '22222' set message_text = "invalid name";
	end if;

	if (new.marks is null) or (new.marks < 0) or (new.marks > 100) then
		signal SQLSTATE '33333' set message_text = "invalid marks";
	end if;
		
	if (new.email is null) or (length(trim(new.email)) = 0) then
		signal SQLSTATE '44444' set message_text = "invalid email";
	end if;  
end $$

