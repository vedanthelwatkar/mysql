-- wamp to add two integers supplied and print their result

use kc_27dec22;
delimiter $$
drop procedure if exists pr1 $$
create procedure pr1(n1 int,n2 int)
begin
	select concat("res of addn = ",n1 + n2) as RESULT;
end $$
delimiter ;