use tcs_27dec22;
delimiter $$
drop procedure if exists pr10 $$
create procedure pr10(i int)
begin
	declare co int default 0;
	declare na varchar(20) default "";
	declare sa decimal(10,2) default 0.0;
	if i is null then
		select "id is null" as ERROR_MSG;
	else
		select count(*) into co from emp where id = i;
		if co = 0 then
			select "emp does not exists" as MSG;
		else
			select name,salary into na,sa from emp where id = i;
			select concat("name = ",na , " salary = ",sa) as MSG;
		end if;
	end if;
end $$
delimiter ;