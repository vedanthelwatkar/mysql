-- wamf to accept as input eid and return ename


use kc_3jan23;
delimiter $$
drop function if exists f2 $$
create function f2(loc varchar(30)) returns int deterministic
begin
declare co int default 0;
select count(*) into co from emp where location = loc;
return co;
end $$
delimiter ;