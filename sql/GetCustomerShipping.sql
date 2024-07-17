delimiter $$
DROP PROCEDURE if EXISTS GetCustomerShipping;

CREATE PROCEDURE GetCustomerShipping( in pcustomernumber int, out pshipping varchar(60))
BEGIN

	declare customercountry varchar(100);
	select country into customercountry
	from customers where customernumber = pcustomernumber;
	
	CASE customercountry
		WHEN 'USA' THEN
			set pshipping = '2-DAY SHIPPING';
		WHEN 'CANADA' THEN
			SET pshipping = '3-DAY SHIPPING';
		WHEN 'Belgium' or 'Italy' THEN
			SET pshipping = '4-DAY SHIPPING';
		ELSE
			set pshipping = '4-DAY SHIPPING';
		END CASE;
END $$
delimiter ;

CALL GetCustomerLevel(484, @shippingduration);
