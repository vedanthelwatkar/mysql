-- create table sa_bkup like sa;(from cmd)


use sbi_4jan23;
delimiter $$
drop event if exists e1 $$
create event e1 on schedule every 30 second do
begin
	delete from sa_bkup;
	insert into sa_bkup select * from sa;
end $$
delimiter ;
