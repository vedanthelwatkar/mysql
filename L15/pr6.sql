-- wamp to generate random motivational quotes


drop database if exists vd_22;
create database if not exists vd_22;
use vd_22;
delimiter $$
drop procedure if exists pr6 $$
create procedure pr6()
begin
declare r int;
declare co int;

create table if not exists messages
(
id int primary key auto_increment,
msg varchar(50)
);