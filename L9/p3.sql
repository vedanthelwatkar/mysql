use kc_22dec22;

drop table if exists java;
drop table if exists python;
create table if not exists java(name varchar(20));
create table if not exists python ( name varchar (20));
insert into java values ("amit") , ("neha");
insert into python values ("amit"), ("sumit") , ("rumit");

-- all students
(select * from java) union (select * from python);
(select * from java) union all (select * from python);

-- common students
( select * from java) intersect ( select * from python);
select * from java,python where java.name=python.name;
select java.name from java,python where java.name=python.name;
select * from java join python using (name); 


-- java - python

( select * from java) except ( select * from python);
select java.name from java left join python on java.name=python.name where python.name is null;

-- python - java

(select * from python) except (select * from java);
select python.name from java right join python on java.name=python.name where java.name is null;