


drop database if exists vendors_db;
create database if not exists vendors_db;
use vendors_db;

drop table if exists vendors;
create table if not exists vendors
(
	vendor_name varchar(20) not null,
	vendor_description varchar(500) not null,
	vendor_phone bigint not null
);

desc vendors;

alter table vendors add column vendor_location varchar(50);
desc vendors;
alter table vendors modify vendor_name varchar(30) not null;
desc vendors;
alter table vendors add column vendor_id int unsigned not null first;
desc vendors;
alter table vendors change vendor_name enum("FLIPKART" ,"AMAZON");
desc vendors;
alter table vendors drop column vendor_phone;
desc vendors;
select * from vendors;