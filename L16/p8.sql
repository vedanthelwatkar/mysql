drop database if exists kp_30dec22;
create database if not exists kp_30dec22;
use kp_30dec22;

create table if not exists book
(
id int unsigned primary key,
title varchar(30),
price decimal(10,2)
);

desc book;