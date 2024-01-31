-- I/P ==> kamal sir ==> title case ==> Kamal Sir

use kc_29dec22;
delimiter $$
drop procedure if exists pr3 $$
create procedure pr3 (fn varchar(20), ln varchar (20))
begin
	declare res varchar(50) default "";
	declare f varchar(20) default "";
	declare l varchar(20) default "";
	if (fn is null) then
		select concat_ws(" ",fn,"cannot be null") as ERROR_MSG;
	elseif (ln is null) then
		select concat_ws(" ",ln,"cannot be null") as ERROR_MSG;
	else
		set f = concat(upper(substring(fn,1,1)),lower(substring(fn,2,length(fn))));
		set l = concat(upper(substring(ln,1,1)),lower(substring(ln,2,length(ln))));
		set res = concat_ws(" ",f,l);
		select res as MSG;
	end if;
end $$
delimiter ; 