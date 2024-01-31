/*wams to create databse and table */

drop database if exists ks_14dec22;
create database if not exists ks_14dec22;
use ks_14dec22;
create table if not exists dept
(
	stno tinyint unsigned primary key,
	dvsn varchar(20) not null,
	hod varchar(20)
);

desc dept;
select * from dept;
insert into dept values(10,"A","amit");
insert into dept values(20,"B","manoj");
insert into dept values(30,"C","vedant");
select * from dept;
