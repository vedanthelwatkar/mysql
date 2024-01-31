-- P1 ==> add using while do
-- P2 ==> add using repeat until
-- P3 ==>  wamp to find fact of integer using while\

use kc_2jan23;
delimiter $$
drop procedure if exists p3 $$
create procedure p3 (num int)
begin
declare i int default 1;
declare fact double default 1;

if num is null then
	select "invalid input" as ERROR_MSG;
elseif num <=0 then
	select "-ve input not allowed" as ERROR_MSG;
else
	while i <= num do
		set fact = fact *  i;
		set i = i  + 1;
	end while;
	select fact as MSG;
end if;
end $$
delimiter ;