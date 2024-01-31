use kit_28dec22;

delimiter $$
drop procedure if exists p2 $$
create procedure p2 (r int)
begin
	declare co int default 0;
	declare na varchar(20) default "";
	declare ma int default 0;
	declare res varchar(20) default "";
	declare ans varchar(100) default "";
	if r is null then
		select concat(r, "rno cannot be null") as ERROR_MSG;
	else
		select count(*) into co from student where rno=r;
		if co = 0 then
			select " rno does not exists " as ERROR_MSG;
		else
			select name,marks into na,ma from student where rno=r;
			if ma >= 70 then
				set res = "Distinction";
			elseif ma >= 60 then
				set res = "First Class";
			elseif ma >=50 then
				set res = "Second Class";
			elseif ma >= 40 then
				set res = "Pass Class";
			else 
				set res = "Fail";
			end if;
				set ans = concat("rno: ",r," - name: ",na," - result: ",res);
				select ans as MSG;
		end if;
	end if;
end $$
delimiter ;