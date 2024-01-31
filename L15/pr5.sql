-- wamp to generate a random integer
-- 5			0 to 4
-- 7			0 to 6

use kc_29dec22;
delimiter $$
drop procedure if exists pr5 $$
create procedure pr5(num int)
begin	
	declare ans int default 0;
		
	if num is null then
		select concat(i , "cannot be null") as ERROR_MSG;
	elseif num <=0 then
		select "Invalid input" as ERROR_MSG;
	else
		set ans = floor(rand() * num) ;
		select ans as MSG;
	end if;
end $$
delimiter ;
