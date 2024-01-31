use kc_28dec22;
delimiter $$
drop procedure if exists pr6 $$
create procedure pr6(d varchar(20))
begin

	if d is null then
		select " null not allowed " as ERROR_MSG;
	else
		case d
			when	"mon"	then	select "weekday" as MSG;
			when	"tue"	then	select "weekday" as MSG;
			when	"wed"	then	select "weekday" as MSG;
			when	"thur"	then	select "weekday" as MSG;
			when	"fri"	then	select "weekday" as MSG;
			when	"sat"	then	select "weekend" as MSG;
			when	"sun"	then	select "weekend" as MSG;
			else			select "invalid input" as ERROR_MSG;
		end case;
	end if;
end $$
delimiter ;