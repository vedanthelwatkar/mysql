use kit_28dec22;
delimiter $$
drop procedure if exists p3 $$
create procedure p3 (r int)
begin
	declare co int default 0;
	declare ey varchar(5) ;
	declare res varchar(20) default "";
	declare ans varchar (100) default "";
	if r is null then
		select "rno can't be null" as ERROR_MSG;
	else
		select count(*) into co from student where rno=r;
		if co = 0 then
			select concat (r,"does not exists") as MSG;
		else
			select eyear into ey from student where rno = r;
			case ey
				when "fe"	then	set res ="5 days";
				when "se"	then	set res= "4 days";
			else				set res= "2 days";
			end case;
			set ans = concat("number of holidys =", res);
			select ans as MSG; 
		end if;	
	end if;
end $$
delimiter ;