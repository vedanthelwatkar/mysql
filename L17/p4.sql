-- P4 ==>  wamp to find fact of integer using repeat until

use kc_2jan23;
delimiter $$
drop procedure if exists p4 $$
create procedure p4 (num int)
begin
declare i int default 1;
declare fact double default 1;

if num is null then
	select "invalid input null not allowed" as ERROR_MSG;
elseif num <=0 then
	select "-ve input not allowed" as ERROR_MSG;
else
	repeat 
		set fact = fact * i;
		set i = i + 1;
	until i > num
	end repeat;
	select concat("fact = ",fact) as MSG;
end if;
end $$
delimiter ;