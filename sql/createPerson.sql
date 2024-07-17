use classicmodels;

drop procedure if exists CreatePerson;

Delimeter $$
Create PROCEDURE CreatePerson()
BEGIN
drop table if Exists persons;
create table persons(
id int auto_increment primary key,
first_name varchar(255) not null,
last_name varchar(255) not null
);

insert into persons(first_name,last_name)
values
('Parag','Joshi'),
('Prachi','Joshi'),
('Manas','Joshi'),
('daesha','Joshi');


select  id , concat (first_name,' ',last_name) as "Person Name" from persons;

end $$
Delimiter ;