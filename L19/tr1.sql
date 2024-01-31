use sbi_4jan23;
delimiter $$
drop procedure if exists pr1 $$
create procedure pr1(src int,dest int,amt int)
begin
update sa set balance = balance + amt where ano = dest;
update sa set balance = balance - amt where ano = src;
select "done" as MSG;
end $$
delimiter ;