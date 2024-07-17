USE classicmodels;
DROP PROCEDURE IF EXISTS GetCustomerLevel;
DELIMITER $$

CREATE PROCEDURE GetCustomerLevel(
IN pcustomernumber INT, 
OUT pcustomerlevel VARCHAR(20)
)
BEGIN
DECLARE credit DECIMAL(10,2) DEFAULT 0;

SELECT creditlimit INTO credit
FROM customers 
WHERE customernumber = pcustomernumber;

IF credit > 50000 THEN
SET pcustomerlevel = 'PLATINUM';
ELSEIF credit <=50000 and credit >10000 THEN
SET pcustomerlevel = 'GOLD';
ELSE 
SET pcustomerlevel = 'NON-PLATINUM';
END IF;
END$$

DELIMITER ;

CALL GetCustomerLevel(484, @level);
