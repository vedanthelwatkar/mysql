use kit_28dec22;

delimiter $$

drop procedure if exists p4 $$
create procedure p4(r int)
begin
	declare co int default 0;
	declare grade varchar(20) default "";
	declare na varchar(20) default "";
	declare ma int default 0;
	declare ans varchar(100) default "";
	if r is null then
		select concat(r," can't be null") as ERROR_MSG;
	else
		select count(*) into co from student where rno = r;
		if co = 0 then
			select concat(r," does not exist") as ERROR_MSG;
		else
			select name,marks into na,ma from student where rno=r;
			if ma > 70 then
				set grade = "A";
			elseif ma > 60 then
				set grade = "B";
			else 
				set grade = "C";
			end if;
				set ans = concat("name = ",na,"  marks = ",ma,"  Grade = ", grade);
				select ans as MSG;
		end if;
	end if;
end $$
delimiter ;