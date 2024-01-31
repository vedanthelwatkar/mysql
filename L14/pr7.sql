use kc_28dec22;
delimiter $$
drop procedure if exists pr7 $$
create procedure pr7(d varchar(20))
begin
	if d is null then
		select " null not allowed" as ERROR_MSG;
	else
		case
			when d= "mon"	then	select "weekday" as MSG;	
			when d= "tue"		then	select "weekday" as MSG;
			when d= "wed"	then	select "weekday" as MSG;
			when d= "thur"	then	select "weekday" as MSG;
			when d= "fri"		then	select "weekday" as MSG;
			when d= "sat"		then	select "weekend" as MSG;
			when d= "sun"	then	select "weekend" as MSG;
		else				select "invalid input" as ERROR_MSG;
		end case;
	end if;
end $$
delimiter ;