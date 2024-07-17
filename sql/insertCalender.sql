USE classicmodels;
DROP PROCEDURE IF EXISTS insertCalendar;
DELIMITER $$

CREATE PROCEDURE insertCalendar(
currebtDate Date
)
BEGIN
insert into calenders (date,month,quarter,year)
values
(currebtDate,month(currebtDate),quarter(currebtDate),year(currebtDate));
END$$
DELIMITER ;
