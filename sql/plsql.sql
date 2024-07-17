create database dvdrental;
CREATE DATABASE
DROP DATABASE dvdrental;
CREATE DATABASE dvdrental ;
\l - list the databases

exit
got to program file \ bin and 

pg_restore - U postgres -d dvdrental path\dvdrental.tar

psql -U postgres

\c dvdrental - connect to the database dvdrental
\dt - list down the tables in dvdrental

SELECT * from customers;
SELECT FIRST_NAME from customers;
SELECT FIRST_NAME,LAST_NAME,EMAIL FROM customer;
SELECT first_name || ' ' || last_name as fullname ,email from customer;

to clear screen:
\! cls

SELECT now(); // current date and time
SELECT first_name || ' ' || last_name as "full name" ,email from customer;

SELECT first_name || ' ' || last_name as "full name" ,email from customer order by first_name asc,last_name desc;

select email,length(email) as lenemail from customer orderby lenemail desc;

create table sort_demo(num,int);
create table
insert into sort_demo(num) values
(1),
(2),
(3),
(null);

select * from sort_demo order by  num desc nulls last;
select * from sort_demo order by  num desc nulls first;

select distinct district,city_id from address;
\d address - give you the details about the tables


select * from address where sistrict = 'LIMA';

Operators used with where clause

= -> Equal
> -> Greater than
< - Less than 
>= Greater than equal to
<= less than equal to 
<> or != -> Not equal
And -> Logical OPERATOR AND
OR -> Logical operator OR
IN -> returns true if value matches any value in the list
Between -> returns true if a value matches a pattern
is Null -> reurns true if value is null
Not -> Negate the result of other options
select last_name,first_name from customer where from customer where first_name ='Jamie';

select last_name,first_name from customer where from customer where first_name ='Jamie' and last_name = 'Rice';

select last_name,first_name from customer where from customer where first_name ='Jamie' or last_name = 'Rice';

select last_name,first_name from customer where from customer where first_name In ('Ann','Anne','Annie');

select last_name,first_name from customer where from customer where first_name like 'Ann%';

select last_name,first_name,length(first_name) from customer where from customer where first_name like 'A%'
and length(first_name) between 3 and 5;


select first_name,last_name  from customer where first_name like 'Bra%' and last_name <> 'Motley';

select film_id ,title,release_year from film order by film_id limit 5;

select film_id ,title,release_year from film order by film_id limit 5 offset 3;
select film_id ,title,release_year from film order by film_id limit 1 offset 3;

select film_id ,title,release_year from film order by film_id desc limit 5 ;




 select film_id ,title,release_year,rating from film order by rating limit 5;
select film_id ,title,release_year,rating from film order by rating limit 5 offset 3;
select film_id ,title,release_year,rating from film order by rating limit 1 offset 3;

select film_id ,title,release_year,rating from film order by rating desc limit 5 ;





select film_id ,title,release_year from film order by film_id fetch first row only ;



select payment_id,amount,payment_date from payment where payment_date :: date in ('2007-02-15', '2007-02-16');

select payment_id,amount,payment_date from payment where payment_date :: date not in ('2007-02-15', '2007-02-16');

select payment_id,amount,payment_date from payment where payment_date between '2007-02-15' and '2007-02-16';

select first_name,last_name from customer where first_name like 'Dar%';

/* //case sensitive pattern search */
select first_name,last_name from customer where first_name ~~ 'Dar%';
/* //case insensitive
 */
 select first_name,last_name from customer where first_name ~~* 'Dar%';

create  table t (message text);
insert into t(message) values ('the rents are now 10% higher than last month ');

select * from t where message like '%10$%%' escape '$';

select address,address2 from address where address2 not null;


select customer_id,sum(amount) from payment group by customer_id order by sum(amount) desc ;

select staff_id ,count(payment_id) from payment group by staff_id;

select customer_id,sum(amount) from payment group by customer_id having sum(amount) > 200
order by sum(amount) desc;

select rating,special_features,count( release_year) from film 
group by rollup(rating,special_features);

