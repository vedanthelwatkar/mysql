-- wamp to add two integers and print the resullt



use kc_26dec22;
delimiter $$
drop procedure if exists pr3 $$
create procedure if not exists pr3(n1 int , n2 int )
begin
declare res int default 0;
declare msg varchar(40) default "";
set res = n1 + n2;
set msg = concat("res of addn ", res);
select msg as MESSAGE;
end $$

delimiter ;

call pr3(10,20);

