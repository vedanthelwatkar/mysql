drop database if exists sbi_4jan23;
create database if not exists sbi_4jan23;
use sbi_4jan23;

create table if not exists sa
(
ano bigint unsigned primary key,
name varchar(50) not null,
balance double unsigned not null
);
desc sa;

delimiter $$
drop trigger if exists t1 $$
create trigger t1 before insert on sa for each row
begin
	if (new.ano is null)  or (new.ano < 1) then
		signal SQLSTATE '12345' set message_text = "invalid account number";
	end if;

	if (new.name is null) or (length(trim(new.name)) = 0 ) or 
		(length(trim(new.name)) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if (new.balance is null) or (new.balance < 3000) then
		signal SQLSTATE '34567' set message_text = "balance shoud be minimum 3000";
	end if;
end $$

drop trigger if exists t2 $$
create trigger t2 before update on sa for each row
begin
	if (new.ano is null)  or (new.ano < 1) then
		signal SQLSTATE '12345' set message_text = "invalid account number";
	end if;

	if (new.name is null) or (length(trim(new.name)) = 0 ) or 
		(length(trim(new.name)) < 2) or (not new.name regexp "^[A-Za-z ]+$") then
		signal SQLSTATE '23456' set message_text = "invalid name";
	end if;
	
	if (new.balance is null) or (new.balance < 3000) then
		signal SQLSTATE '34567' set message_text = "balance shoud be minimum 3000";
	end if;
end $$
delimiter ;
