CREATE TABLE employee (
    empno INT,
    ename VARCHAR(50),
    job VARCHAR(50),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(10, 2),
    comm DECIMAL(10, 2),
    deptno INT
);


INSERT INTO employee (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(8369, 'SMITH', 'CLERK', 8902, '1990-12-18', 800.00, NULL, 20),
(8499, 'ANYA', 'SALESMAN', 8698, '1991-02-20', 1600.00, 300.00, 30),
(8521, 'SETH', 'SALESMAN', 8698, '1991-02-22', 1250.00, 500.00, 30),
(8566, 'MAHADEVAN', 'MANAGER', 8839, '1991-04-02', 2985.00, NULL, 20),
(8654, 'MOMIN', 'SALESMAN', 8698, '1991-09-28', 1250.00, 1400.00, 30),
(8698, 'BINA', 'MANAGER', 8839, '1991-05-01', 2850.00, NULL, 30),
(8882, 'SHIVANSH', 'MANAGER', 8839, '1991-06-09', 2450.00, NULL, 10),
(8888, 'SCOTT', 'ANALYST', 8566, '1992-12-09', 3000.00, NULL, 20),
(8839, 'AMIR', 'PRESIDENT', NULL, '1991-11-18', 5000.00, NULL, 10),
(8844, 'KULDEEP', 'SALESMAN', 8698, '1991-09-08', 1500.00, 0.00, 30);

. Consider the Empl table and write SQL command to get the following.
a. Write a query to display EName and Sal of employees whose salary are greater than  or equal to 2200?
select ename,sal from employee where sal>=2200;

b. Write a query to display details of employs who are not getting commission?
select ename from employee where comm is  null;
 
c. Write a query to display employee name and salary of those employees who don’t have  their salary in range of 2500 to 4000?
select ename,sal from employee where sal not between 2500 and 4000;

d. Write a query to display the name, job title and salary of employees who don’t have manager?
select ename,job,sal from employee where mgr is null;

e. Write a query to display the name of employee whose name contains “A” as third alphabet?
select ename from employee where ename like '__A%';

f. Write a query to display the name of employee whose name contains “T” as last alphabet?
select ename from employee where ename like '%T';

g. Write a query to display the name of employee whose name contains ”M” as First and “L” as third alphabet?
select ename from employee where ename like 'M_L%';

h. Write a query to display details of employs with the text “Not given”, if commission is null?

select ename,ifnull(comm, 'Not given') as commission from employee where comm is null ;
