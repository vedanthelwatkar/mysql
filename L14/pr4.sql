-- wamp to acept as input an integer and check if its even or odd


use kc_28dec22;
delimiter $$
drop procedure if exists pr3 $$
create procedure pr3(num int)
begin
	if num is null then
		select " null not allowed " as ERROR_MSG;
	else
		case num % 2
			when num % 2 = 0	then select "even" as MSG;
			when num % 2 = 1	then select "odd" as MSG;
			when num % 2 = -1	then select "odd" as MSG;	 
		end case;
	end if;
end $$
delimiter ;