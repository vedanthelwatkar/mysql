-- wamp to accept as nput an integer and check if its even or odd

use kc_28dec22;
delimiter $$
drop procedure if exists pr1 $$
create procedure pr1(num int)
begin
	if num is null then
		select "null not allowed" as ERROR_MSG;
	else		
		if num % 2 = 0 then
			select "even" as RESULT;
		else 
			select "odd" as RESULT;
		end if;
	end if;
end $$
delimiter ;