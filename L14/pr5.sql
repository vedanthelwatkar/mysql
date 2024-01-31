-- wamp to read marks and print grade

use kc_28dec22;
delimiter $$
drop procedure if exists pr5 $$
create procedure pr5(marks int)
begin
	if marks is null then
		select " invalid input " as ERROR_MSG;
	else
		if  (marks < 0) or (marks > 100) then
			select "marks must be between 0 to 100" as ERROR_MSG;
		elseif (marks > 80) then
			select " A " as GRADE;
		elseif (marks > 60) then
			select "B" as GRADE;
		elseif (marks > 40) then
			select "C" as GRADE;
		else
			select "D" as GRADE;
		end if;
	end if;
end $$
delimiter ;	
		