-- wamp to accept as input three numbers and
-- print their sum and avg

use kc_27dec22;
delimiter $$
drop procedure if exists pr4 $$
create procedure pr4(n1 double,n2 double,n3 double)
begin
	declare sum double default 0.0;
	declare avg double default 0.0;
	declare msg varchar(50) default "";
	set sum = n1 + n2 + n3;
	set avg = sum / 3;
	set msg= concat("sum = ",round(sum,2) and "avg = ",round(avg,2));
	select msg as RESULT;
end $$
delimiter ;
