Craete view customerPayments
as
select customername,checknumber,paymentdate,amount
from customers
inner join 
payments using(customernumber)


Create or replace view customerPayments AS
select customername as cname,checknumber as cheque,paymentdate,amount
from customers
inner join 
payments using(customernumber)