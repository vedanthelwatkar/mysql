--  wamp to accept as input first and last name and primt 
-- them together with firstname in uppercase and lastname in lowercase
-- provided they are not null

use kc_29dec22;
delimiter $$
drop procedure if exists pr1 $$
create procedure pr1(fn varchar(20), ln varchar(20))
begin 
	declare res varchar(50) default "";
	if fn is null then
		select "first name null not allowed" as ERROR_MSG;
	elseif ln is null then
		select "last name null not allowed" as ERROR_MSG;
	else
		set res = concat_ws(" ",upper(fn),lower(ln));
		select res as MSG;
	end if;
end $$
delimiter ;
