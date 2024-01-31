drop database if exists  kit_28dec22;
create database if not exists kit_28dec22;
use kit_28dec22;

create table if not exists student
(
rno int unsigned primary key,
name varchar(20),
marks tinyint unsigned,
eyear enum ("fe","se","te","be"),
location varchar(30) default "mumbai"
);
desc student;

insert into student values (10,"amit",98,"fe","thane");
insert into student values (20,"sumit",79,"se","mumbai");
insert into student values (30,"rumit",63,"fe","thane");
insert into student values (40,"seema",81,"se","thane");
insert into student values (50,"reema",45,"fe","mumbai");
insert into student values (60,"tina",95,"be","thane");

select  * from student;


use kit_28dec22;
delimiter $$
drop procedure if exists p1 $$
create procedure p2(r int)
begin
	declare co int default 0;
	declare na varchar(20) default "";
	declare ma tinyint default 0;
	declare res varchar(20) default "";
	declare ans varchar (100) default "";
	if r is null then
		select "rno can't be null" as ERROR_MSG;
	else
		select count(*) into co from student where rno=r;
		if co = 0 then
			select concat (r,"does not exists") as MSG;
		else
			select name,marks into na,ma from student where rno=r;
			if ma > 60 then
				set res= "PASS";
			else
				set res = "FAIL";
			end if;
			set ans = concat("rno",r,"name",na,"result",res);
			select ans as MSG;
		end if;
	end if;
end $$
delimiter ;