-- this is soln to pract 4

use variety_infotech_db;

create or replace view prod_over as
select * from products where pstock=0;
select * from prod_over;


create or replace view prod_list as 
select pname from products;
select * from prod_list;


create or replace view prod_price as
select pname as product_name, pprice as product_price from products;
select * from prod_price;
-- can be also done as
create or replace view pord_price2 as (product_name,product_price) 
select pname,pprice from products;
select * from prod_price2;



create or replace view prod_storage as
select pname , pprice from products where pname in ("hdd","cd","sd card");
select * from prod_storage;


create or replace view prod_top2 as
select pname,pprice from products
order by pprice desc limit 2;
select * from prod_top2;
