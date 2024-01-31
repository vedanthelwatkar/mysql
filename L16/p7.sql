use kc_30dec22;
delimiter $$
drop procedure if exists p7 $$
create procedure p7()
begin
declare table_nahi_hai condition for 1146;
declare exit handler for table_nahi_hai
select "table does not exists" as ERROR_MSG;
select "Good Evening" as MSG;
select * from employee;
Select "Bye" as MSG;
end $$
delimiter ;
