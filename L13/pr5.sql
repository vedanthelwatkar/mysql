-- wamp to accept as input three numbers and print sum and avg

use kc_27dec22;
delimiter $$
drop procedure if exists pr5;
create procedure pr5(n1 double,n2 double,n3 double,out sum double,out avg double)
begin
	set sum = n1 + n2 + n3;
	set sum = round(sum,2);
	set avg = sum / 3;
	set avg = round(avg,2);
end $$
delimiter ;