-- wamf to accept as input eid and return ename

use kc_3jan23;
delimiter $$
drop function if exists f3 $$
create function f3(i int) returns varchar(20) deterministic
begin
declare co int default 0;
declare na varchar(20) default "";

select count(*) into co from emp where i = id;
if co = 0 then
	set na = "emp  does not exists";
else
	select name into na from emp where id = i;
end if;
return na;
end $$
delimiter ;