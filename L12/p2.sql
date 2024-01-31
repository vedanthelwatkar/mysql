-- this is pract 3

drop database if exists variety_infotech_db;
create database if not exists variety_infotech_db;
use variety_infotech_db;

create table if not exists products
(
pid tinyint unsigned primary key auto_increment,
pname varchar(20) not null,
pprice decimal(10,2) not null,
pstock tinyint unsigned
);

insert into products value(101,"hdd",5200.00,10);
insert into products value(default,"cd",180.00,20);
insert into products value(default,"speaker",1500.00,5);
insert into products value(default,"keyboard",850.00,10);
insert into products value(default,"sd card",475.00,0);

select * from products;

