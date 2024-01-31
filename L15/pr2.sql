-- wamp to accept as input a string and check if its a palnidrome

use kc_29dec22;
delimiter $$
drop procedure if exists pr2 $$
create procedure pr2(str varchar(50))
begin
	declare rstr varchar(50);
	if (str is null) then
		select concat_ws(" ",str,"cannot be null") as ERROR_MSG;
	else 
		set rstr = reverse(str);
		if str = rstr then
			select "It is a palindrome" as MSG;
		else
			select "It is not a palindrome" as MSG;
		end if;
	end if;
end $$
delimiter ;