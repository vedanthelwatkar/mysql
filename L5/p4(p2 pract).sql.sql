#wamss to create a database vendors_db

drop database if exists vendors_db;
create database if not exists vendors_db;
use vendors_db;

drop table if exists vendors;
create table if not exists vendors
(
vendor_name varchar(20) not null,
vendor_description varchar(500) not null,
vendor_phone bigint(10) not null
);

desc vendors;

alter table vendors add column vendor_location varchar(50);
alter table vendors modify vendor_name varchar(30) not null;
alter table vendors add column vendor_id smallint unsigned not null first;
alter table vendors modify vendor_name enum("FLIPKART","AMAZON");
alter table vendors drop vendor_phone;
desc vendors;