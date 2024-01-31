-- wamp to accept as input radius and print area and circum of circle

use kc_27dec22;
delimiter $$
drop procedure if exists pr6 $$
create  procedure pr6 (radius double)
begin
	declare area double default 0.0;
	declare circum double default 0.0;
	declare pi double default 3.14159;
	declare msg varchar(50) default "";
	if radius is null then
		set msg = "Invalid input";
		select msg as ERROR;
	elseif radius < 0.0 then
		set msg = " -ve radius not allowed";
		select msg as ERROR;
	else
		set area = pi * radius * radius;
		set area = round(area,2);
		set circum = 2 * pi * radius;
		set circum = round(circum,2);
		set msg = concat ("area = ",area ,"circum = ",circum);
		select msg as RESULT;
	end if;
end $$
delimiter ;