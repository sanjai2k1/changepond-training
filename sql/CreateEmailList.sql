USE classicmodels;
DROP PROCEDURE IF EXISTS Create_Email_List;
DELIMITER $$

CREATE PROCEDURE Create_Email_List(
inout email_list TEXT
)
BEGIN
declare email_address  varchar(100) default "";
declare done bool default false;

declare cur_email_list CURSOR for select email from employees;

declare continue HANDLER
for not found set done = true;

open cur_email_list;
set email_list = '';
process_email : LOOP
fetch cur_email_list into email_address;
if done = true then
LEAVE process_email;
end if;
set email_list=concat(email_address,";",email_list);
end loop;
close cur_email_list;

END$$
DELIMITER ;







USE classicmodels;
DROP PROCEDURE IF EXISTS Create_Email_List;
DELIMITER $$

CREATE PROCEDURE Create_Email_List(
inout email_list TEXT
)
BEGIN
declare email_address  varchar(100) default "";
declare done bool default false;

declare cur_email_list CURSOR for select email from employees;

declare continue HANDLER
for not found set done = true;

open cur_email_list;
set email_list = '';
while done = false do
fetch cur_email_list into email_address;
set email_list=concat(email_address,";",email_list);
end while;
close cur_email_list;

END$$
DELIMITER ;
