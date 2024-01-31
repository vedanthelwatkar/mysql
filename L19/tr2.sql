use sbi_4jan23;
delimiter $$
drop procedure if exists tr2 $$
create procedure tr2 (src int, dest  int,amt int)
begin
declare issue boolean default false;

declare continue handler for SQLException
begin
	show errors;
	set issue = true;
end;

start transactions;
	update sa set balance = balance + amt where ano = dest;
	update sa set baance = balance - amt where ano = src;

if not issue then
	commit;
	select "SUCCESS!" as MSG;
else
	rollback;
	select "FAILURE" as MSG;
end if;
end $$
delimiter ;