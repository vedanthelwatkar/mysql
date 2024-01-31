-- wamp to add two integers supplied and print their result

use kc_27dec22;
delimiter $$
drop procedure if exists pr2 $$
create procedure pr2 (n1 int,n2 int)
begin
	declare res int default 0;
	declare msg varchar(50) default "";
	set res = n1 + n2;
	set msg = concat ("res of addn = ", res); 
	select msg as RESULT;
end $$
delimiter ;
