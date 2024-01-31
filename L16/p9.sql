use kp_30dec22;
delimiter $$
drop procedure if exists p9 $$
create procedure p9(i int, t varchar(40),p decimal(20,2))
begin

declare exit handler for 1062
select "id already exists" as ERROR_MSG;

declare exit handler for 1264
select "invalid id / price" as ERROR_MSG;

declare exit handler for 1048
select "id cannot be null" as ERROR_MSG; 

declare exit handler for 1265
select "title cannot be more than 30 characters" as ERROR_MSG;

declare exit handler for SQLSTATE '12345'
select "title cannot be null" as ERROR_MSG;

declare exit handler for SQLSTATE '23456'
select "blank title not allowed " as ERROR_MSG;

declare exit handler for  SQLSTATE '34567'
select "title cannot be only spaces" as ERROR_MSG;

declare exit handler for SQLSTATE '45678'
select "price cannot be 0 or -ve" as ERROR_MSG;

if (t is null) then
	signal SQLSTATE '12345';
end if;

if length(t) = 0 then
	signal SQLSTATE '23456';
end if;

if length(trim(t)) = 0 then
	signal SQLSTATE '34567';
end if;

if (p is null) or (p < 1) then 
	signal SQLSTATE '45678';
end if;

insert into book values(i,t,p);
select "Record Inserted" as MSG;

end $$
delimiter ;