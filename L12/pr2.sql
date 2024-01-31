-- wamp to accept the name of user
-- and then welcome the user


delimiter ##

drop procedure if exists pr2 ##
create procedure if not exists pr2(name varchar(20))
begin
declare msg varchar(40) default "";
set msg = concat("welcome ", name);
select msg as MESSAGE;
end ##

delimiter ;

call pr2("thakur");
