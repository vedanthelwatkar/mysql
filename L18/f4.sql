-- wampf to return sum and avg salary

use kc_3jan23;
delimiter $$
drop function if exists f4 $$
create function f4() returns varchar(100) deterministic
begin
declare su float default 0;
declare av float default 0;
declare re varchar(100) default "";
select sum(salary),avg(salary) into su,av from emp;
set re = concat("sum = ",su," avg = ",av);
return re;
end $$
delimiter ;