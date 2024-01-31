-- wamp to accept as integrr an integer and check if iots even or odd

use kc_28dec22;
delimiter $$
drop procedure if exists pr2 $$
create procedure pr2(num int)
begin
	if num is null then
		select "null not allowed " as ERROR_MSG;
	else
		case num % 2
			when 0	then select "even " as MSG;
			when 1	then select "odd" as MSG;
			when -1 	then select "odd" as MSG;
		end case;
	end if;
end $$
delimiter ;