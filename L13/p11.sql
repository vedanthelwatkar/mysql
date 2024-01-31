use tcs_27dec22;
delimiter $$
drop procedure if exists pr11 $$
create procedure pr11(i int,out s decimal (10,2))
begin
	declare co int default 0;
	if i is null then
		select "id is nnull" as ERROR_MSG;
	else
		select count(*) into co from emp where id = i;
		if co = 0 then
			select "emp does not exist" as MSG;
		else 
			select salary into s from emp where id = i;
		end if;
	end if;
end $$
delimiter ;

		