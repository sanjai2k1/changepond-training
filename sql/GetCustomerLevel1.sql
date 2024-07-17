USE classicmodels;
DROP function IF EXISTS CustomerLevel;

DELIMITER $$
CREATE function CustomerLevel(
credit DECIMAL(10,2)
)
returns varchar(20)
Deterministic
BEGIN
DECLARE customerLevel varchar(20) ;



IF credit > 50000 THEN
SET customerLevel = 'PLATINUM';
ELSEIF credit <=50000 and credit >10000 THEN
SET customerLevel = 'GOLD';
ELSE 
SET customerLevel = 'SILVER';
END IF;
return (customerLevel);
END$$

DELIMITER ;


CALL GetCustomerLevel(484, @level);
