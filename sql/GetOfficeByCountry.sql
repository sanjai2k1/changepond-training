Delimiter //
create procedure GetOfficeByCountry(In countryName varchar(255))
BEGIN
Select * from offices where country = countryName;
end //
Delimiter ;
