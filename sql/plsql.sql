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

select cust.customer_id,cust.first_name,cust.last_name,p.amount,p.payment_date from customer cust inner join payment p on p.customer_id = cust.customer_id order by p.payment_date;



select cust.customer_id,cust.first_name,cust.last_name,p.amount,p.payment_date from customer cust inner join payment p using(customer_id) order by p.payment_date;


select cust.customer_id,
cust.first_name || ' ' ||cust.last_name "Customer",
s.first_name || ' ' || s.last_name "Staff",
p.amount,p.payment_date from customer cust inner join payment p using(customer_id)
inner join staff s using(staff_id)
 order by p.payment_date;



select f.film_id,f.title,i.inventory_id from film f left join inventory i on i.film_id = f.film_id order by i.inventory_id desc;

select f.film_id,f.title,i.inventory_id from film f right join inventory i on i.film_id = f.film_id order by i.inventory_id desc;


select e.first_name || ' ' || e.last_name Employee,
m.first_name || ' ' || m.last_name Manager 
from employee e left join employee m on m.employee_id = e.manager_id order by Manager;


select c.*,p.* from customer c full outer join payment p on c.customer_id = p.customer_id;

select * from language cross join category;



select city from city where country_id in (select country_id from country where country = 'Argentina');

select title from film where film_id in(
select film_id from film_category where category_id=(
select category_id from category where name = 'Action'));



select film_id,title,length,rating from film f where length (select avg(length) from  film where rating = f.rating);




select first_name,last_name from staff where staff_id = Any (select manager_staff_id from store);


select customer_id,first_name,last_name from customer where customer_id > All (select customer_id from rental where rental_id in (18,25)) order by customer_id;

select customer_id,first_name,last_name from customer c where exists
(select 1 from payment p where p.customer_id = c.customer_id and amount >11);


select release_year from top_rated_films union select release_year from most_popular_films;

select * from top_rated_films union all select * from most_popular_films;

select * from top_rated_films intersect  select * from most_popular_films;


select * from top_rated_films except  select * from most_popular_films;


select sum
(case when rental_rate = 0.99 then 1 else 0 End) as "Economy",
 sum
(case when rental_rate = 2.99 then 1 else 0 End) as "Mass",
 sum
(case when rental_rate = 4.99 then 1 else 0 End) as "Premium"
from film;



select title,rating,
case rating 
when 'G' then 'General Audiences'
when 'PG' then 'Parental Guidance Suggested'
when 'PG-13' then 'Parents Strongly Cautioned'
when 'R' then 'Restricted'
when 'NC-17' then 'Adults Only'
End rating_description
from film;


select distinct(rating) from film;





select sum
(case when rating = 'PG' then 1 else 0 End) as "PG",
 sum
(case when rating = 'R' then 1 else 0 End) as "R",
 sum
(case when rating = 'NC-17' then 1 else 0 End) as "NC-17",
sum
(case when rating = 'PG-13' then 1 else 0 End) as "PG-13",
sum
(case when rating = 'G' then 1 else 0 End) as "G"
from film;


select title,rating,
case rating
	when 'G' then 'General Audiences'
	when 'PG' then 'parental Guidances'
	when 'PG-13' then 'parental strongly Audiences'
	when 'R' then 'Restricted'
	when 'NC-17' then 'Adults only'
		End rating_description
from film;


select collesce(address2,'Pune') from address order by address2 desc;


create table if not exists accounts(
users_id serial primary key,
username varchar(50) unique not null,
password varchar(50) not null,
email varchar(255) unique not null,
last_login timestamp);
);

select film_id,title,rental_rate into table film_r from film where rating='R' and rental_duration = 5
order by title;

create table action_film as select film_id ,title,release_year,length,rating from film inner join film_category using(film_id) where category_id =1;

create table fruits(id serial primary key,name varchar not null );

insert into  fruits (name) values ('orange');
insert into fruits (id,name) values (Default,'grapes');

select currval(pg_get_serial_sequence('fruits','id'));

insert into fruits(name) values ('JackFruit')returning id;




create sequence mysequence increment 5 start 100;


create sequence three increment -1 minvalue 1 maxvalue 3 start 3 cycle;


create table order_details(
order_id serial,
item_id int not null,
item_Text varchar not null,
price dec(10,2) not null,
primary key (order_id,item_id));


create  sequence order_item_id
start 10
increment 10
minvalue 10
owned by order_details.item_id


insert into order_details(order_id,item_id,item_Text,price) values (100,nextval('order_item_id'),'DVD Player',100),
 (100,nextval('order_item_id'),'Android TV',500),
 (100,nextval('order_item_id'),'Speaker',150),
(100,nextval('order_item_id'),'Min Wifi',300);


create table color(
color_id int generated by default as identity
(start with 10 increment by 10),
color_name varchar not null);


insert into color(color_name) values ('Red');
insert into color(color_name) values('purple');
);






create table contacts(id serial primary key,
first_name varchar(50) not null,
last_name  varchar(50) not null,
full_name varchar(101) generated always as (first_name || ' ' || last_name) sorted,
email varchar(300) unique);



insert into contacts (first_name,last_name,email)
values
('Parag','Joshi','parag@gmail.com'),
('Prachi','Joshi','prachi@gmail.com')
returning *;


string Functions:
select ASCII(first_name) from employee;
SELECT CHR(65) AS CodeToCharacter;
SELECT POSITION('t' IN 'Customer') AS MatchPosition;
SELECT CONCAT(first_name,last_name) from employee;
SELECT CONCAT_WS(' ', first_name, last_name) from employee;
SELECT LENGTH(CONCAT_WS(' ', first_name, last_name)) from employee;
SELECT TO_CHAR(123456789, '99-99-99999') AS FormattedNumber;
SELECT LEFT(first_name, 3) AS ExtractString from employee;
SELECT POSITION('San' IN 'Sanjai') AS MatchPosition;
SELECT TRANSLATE('Monday', 'Monday', 'Sunday');
SELECT repeat(first_name, 2) AS RepeatedString from employee;




Math Functions:
SELECT Abs(-243.5) AS AbsNum;
SELECT AVG(Price) AS AveragePrice FROM order_details;
SELECT CEILING(price) AS CeilValue from order_details;
SELECT COUNT(*)  FROM customer;
SELECT FLOOR(price) AS FloorValue from order_details;;
SELECT MIN(Price) AS SmallestPrice FROM order_details;
SELECT MAX(Price) AS LargestPrice FROM order_details;
SELECT POWER(Price, 2)FROM order_details;
SELECT SUM(Price) AS TotalPrice FROM order_details;




Date Functions:
SELECT CURRENT_TIMESTAMP;
SELECT payment_date::date,payment_date::date + INTERVAL '1 year' AS DateAdd from payment;
SELECT (last_update::date - '2016-05-29'::date) AS DateDifference from film;
SELECT EXTRACT(DAY FROM  payment_date ) AS DayOfMonth from payment;
SELECT DATE_PART('day', payment_date ) AS DayOfMonth from payment;
 select now();
SELECT EXTRACT(MONTH FROM payment_date) AS MonthPart FROM payment;
SELECT EXTRACT(YEAR FROM payment_date) AS MonthPart FROM payment;






