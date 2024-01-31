drop database if exists kit_3jan23;
create database if not exists kit_3jan23;
use kit_3jan23;

create table if not exists student
(
rno int unsigned primary key,
name varchar(30) not null,
marks tinyint unsigned
);

delimiter $$
drop trigger if exists t1 $$
create trigger t1 before insert on student for each row
begin
	if ( new.rno is null ) or ( new.rno < 1) then
		signal SQLSTATE '12345' set message_text = "invalid rno";
	end if;
	
	if ( new.name is null) or (length(trim(new.name)) = 0 ) or (length(new.name) < 2) or
		(not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if ( new.marks is null) or (new.marks > 100 ) or (new.marks < 0) then
		signal SQLSTATE '34567' set message_text = "invalid marks";
	end if;
end $$

drop trigger if exists t2 $$
create trigger t2 before update on student for each row
begin
	if ( new.rno is null ) or ( new.rno < 1) then
		signal SQLSTATE '12345' set message_text = "invalid rno";
	end if;
	
	if ( new.name is null) or (length(trim(new.name)) = 0 ) or (length(new.name) < 2) or
		(not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if ( new.marks is null) or (new.marks > 100 ) or (new.marks < 0) then
		signal SQLSTATE '34567' set message_text = "invalid marks";
	end if;
end $$
delimiter ;