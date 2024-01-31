-- wamp to accept as input radius and if its correct print area and circum of circle


use kc_29dec22;
delimiter $$
drop procedure if exists pr4 $$
create procedure pr4(radius float)
begin
	declare area float default 0.0;
	declare circum float default 0.0;
	declare pi float default 3.14159;
	declare res varchar(50) default "";
	if radius is null then
		select "Radius cannot be null" as ERROR_MSG;
	elseif radius < 0 then
		select "Radius cannot be negative" as ERROR_MSG;
	else 
		set area = round(pi * power(radius,2),2);
		set circum = round(2 * pi * round(radius,2),2);
		set res = concat("area =",area," circum = ",circum);
		select res as MSG;
-- 		select round(area,2) as AREA;
-- 		select round(circum,2) as CIRCUMFERENCE;
	end if;
end $$
delimiter ;
	