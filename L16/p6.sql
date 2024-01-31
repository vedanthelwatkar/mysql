use kc_30dec22;
delimiter $$
drop procedure if exists p6 $$
create procedure p6()
begin
declare exit handler for 1146
select "table does not exists" as ERROR_MSG;
select "Good Evening" as MSG;
select * from employee;
select "Bye" as MSG;
end $$
delimiter ;