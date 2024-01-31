-- this is practical 1 (revision)


drop database if exists kc_24dec22;
create database if not exists kc_24dec22;
use kc_24dec22;

create table if not exists courses
(
cid int unsigned primary key,
cname varchar(20) not null,
cprice decimal(10,2) unsigned not null
);
desc courses;

insert into courses values(1,"pfsd",40000.00);
insert into courses values(2,"jfsd",30000.00);
insert into courses values(3,"jsfsd",25000.00);
insert into courses values(4,"aws",35000.00);

select * from courses;

