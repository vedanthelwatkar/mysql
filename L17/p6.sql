use tcs_2jan23;
delimiter $$
drop procedure if exists p6 $$
create procedure p6 (out data varchar(500))
begin
declare na varchar(50) default "";
declare i int default 1;
declare co int default 0;
declare c cursor for select name from emp;
select count(*) into co from emp;
if co = 0 then
	set data = "no data found";
else
	open c;	
	set data = "";
	while i < co do
		fetch c into na;
		set data = concat(data, " ", na);
		set i = i + 1;
	end while;
	close c;
end if;
end $$
delimiter ;