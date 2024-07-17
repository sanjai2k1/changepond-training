USE classicmodels;
DROP PROCEDURE IF EXISTS loadDates;
DELIMITER $$

CREATE PROCEDURE loadDates(
startDate Date, 
day int
)
BEGIN
DECLARE counter int default 0;
DECLARE currebtDate  DATE default startDate;
while counter <=day do 
call InsertCalendar(currebtDate);
set counter = counter+1;
set currebtDate = date_add(currebtDate ,interval 1 day);
end while;

END$$
DELIMITER ;


call loadDates('2024-01-01',365);