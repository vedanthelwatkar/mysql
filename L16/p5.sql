use kc_30dec22;
delimiter $$
drop procedure if exists p5 $$
create procedure p5()
begin
declare continue handler for 1146
select "table does not exists" as ERROR_MSG;

select "Good evening" as MSG;
select * from employee;
select "Bye" as MSG;
end $$
delimiter ;