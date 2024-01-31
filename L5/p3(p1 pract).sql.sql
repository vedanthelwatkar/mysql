#wamss to create a database books_db

drop database if exists books_db;
create database if not exists books_db;
use books_db;

drop table if exists book;
create table if not exists book
(
	book_id tinyint unsigned not null,
	book_name varchar(10),
	author_name varchar(50)
);

desc book;

alter table book add column book_price decimal(10,2) not null;
alter table book modify book_name varchar(30);
alter table book add column publisher_name varchar(100) after book_name;
alter table book modify book_name varchar(30) not null; 
alter table book modify author_name varchar(100) not null;
alter table book modify book_price decimal(10,2) unsigned not null;
desc book;
select * from book;

