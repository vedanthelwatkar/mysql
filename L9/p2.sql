use kc_22dec22;
-- cross join

select * from dept, emp;
select * from dept join emp;
select * from dept cross join emp;


-- inner join

select * from dept, emp where dept.did = emp.did;
select * from dept join emp on dept.did = emp.did;
select * from dept join emp using(did); 
select * from dept natural join emp;
select * from emp natural join dept;

-- equi  join

select * from dept,emp where (dept.did=emp.did) and (dept.dname="sales");

-- non-equi join

select * from dept,emp where (dept.did=emp.did) and (dept.dname!="sales");

-- self join

select a.ename as EMPLOYEE, b.ename as MANAGER from emp a , emp b where a.reports_to = b.eid;

-- left outer join ( since, kamal is missing)

select a.ename as EMPLOYEE , b.ename as MANAGER from emp a left join emp b on a.reports_to = b.eid;
