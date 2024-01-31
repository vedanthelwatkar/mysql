-- wamf to return number of employees

use kc_3jan23;
delimiter $$
drop function if exists f1 $$
create function f1() returns int deterministic
begin
declare co int default 0;
select count(*) into co from emp;
return co;
end $$
delimiter ;