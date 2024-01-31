-- wamp to 

use kc_27dec22;
delimiter $$
drop procedure if exists pr3 $$
create procedure pr3 (in n1 int,in n2 int, out res int)
begin
	set res= n1 + n2;
end $$
delimiter ;