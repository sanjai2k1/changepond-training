USE classicmodels;
DROP PROCEDURE IF EXISTS GetDeliveryTime;
DELIMITER $$

CREATE PROCEDURE GetDeliveryTime(
IN porderNumber INT, 
OUT deliveryTime VARCHAR(20)
)
BEGIN
DECLARE OD DATE;
DECLARE SD DATE;
DECLARE DIFF INT;

SELECT orderDate,shippedDate INTO OD,SD
FROM orders 
WHERE orderNumber = porderNumber;

IF OD IS NULL OR SD IS NULL THEN
SET deliveryTime = 'Not Sufficient Data';
ELSE
SET DIFF = DATEDIFF(SD, OD);
IF DIFF = 0 THEN 
SET deliveryTime = 'Delivery On Time';
ELSEIF DIFF < 0 THEN 
SET deliveryTime = 'Delivery Early';
ELSEIF DIFF > 0 AND DIFF <= 3 THEN 
SET deliveryTime = 'Delivery Late';
ELSEIF DIFF > 3 THEN 
SET deliveryTime = 'Delivery Very Late';
END IF;
END IF;
END$$

DELIMITER ;

CALL GetDeliveryTime(10100, @level);