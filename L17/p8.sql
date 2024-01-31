use tcs_2jan23;
delimiter $$
drop procedure if exists p8 $$
create procedure p8 (de varchar(20),out data varchar(500))
begin
declare i int default 1;
declare na varchar(50) default "";
declare co int default 0;
declare c cursor for select name from emp where dept =de;

select count(*) into co from emp where dept = de;
if co = 0 then
	set data = "no data found";
else
	open c;
	set data = "";
	while i <= co do
		fetch c into na;
		set data = concat (data , "-", na);
		set i = i +1;
	end while;
	close c;
end if;
end $$
delimiter ;