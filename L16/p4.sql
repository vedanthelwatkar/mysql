use kc_30dec22;
delimiter $$
drop procedure if exists p4 $$
create procedure p4()
begin
	select "Good Evening" as MSG;
	select * from employee ;
	select "Bye" as MSG;
end $$
delimiter ;
 