use tcs_2jan23;
delimiter $$
drop procedure if exists p9 $$
create procedure p9 (in loc varchar(20),out data varchar(200))
begin
declare co int default 0;
declare na varchar(20) default "";
declare i int default 1;
declare sa decimal(10,2) default 0;
declare c cursor for select name,salary from emp where location = loc;
select count(*) into co from emp where location = loc;
if co = 0 then
	set data  = "no data found ";
else
	open c;
	set data = "";
	repeat
		fetch c into na,sa;
		set data = concat(data, " ", na, "-" , sa);
		set i = i + 1;
	until i > co
	end repeat;
	close c;
end if;
end $$
delimiter ;