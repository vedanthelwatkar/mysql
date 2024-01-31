-- this is pr1


delimiter $$
drop procedure if exists pr1 $$
create procedure if not exists pr1()
begin
	select "welcome" as MESSAGE;
end $$

delimiter ;

call pr1();