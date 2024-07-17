use classicmodels;
drop procedure if exists GetOrderCountByStatus;
Delimiter //
create procedure GetOrderCountByStatus(In orderstatus varchar(255), out total int)
BEGIN
Select count(ordernumber) into total from orders 
where status = orderstatus;
end //
Delimiter ;

call GetOrderCountByStatus('Shipped',@total);
select @total;


Delimiter //

DROP PROCEDURE if EXISTS GetOrderCountByStatus;


CREATE PROCEDURE GetOrderCountByStatus(IN orderstatus VARCHAR(255), out total int)
BEGIN
select count(orderNumber) into total From orders 
where status = orderstatus;
end //
delimiter ;

call GetOrderCountByStatus('In Process',@total);
select @total;


 select routine_name from information_schema.routines
 where routine_type = 'TABLE'
 and routine_schema = 'classicmodels';