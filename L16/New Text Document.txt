-- p1 and p2 is being revised in p3 
-- with inout parameter

use kc_30dec22;
delimiter $$
drop procedure if exists p3 $$
create procedure p3(inout num double)
begin
	if num is null then
		select "null not allowed " as ERROR_MSG;
	elseif num < 0.0 then
		select "-ve number not allowed" as ERROR_MSG;
	else
		set num = sqrt (num);
		set num = round(num,2);
	end if;
end $$
delimiter ; 
