-- wamp to accept as input two integers 
-- and print the max of two

use kc_27dec22;
delimiter $$
drop procedure if exists pr7 $$
create procedure pr7 (n1 int,n2 int)
begin
	declare res int default 0;
	declare msg varchar(100) default "";
	if n1 is null or n2 is null then
		set msg= "invalid input";
		select msg as ERROR;
	elseif n1>=n2 then
		set res = n1;
		set msg = concat("max of two is", res);
		select msg as RESULT;
	else
		set res = n2;
		set msg = concat("max of two is", res);
		select msg as RESULT;
	end if;
end $$
delimiter ;