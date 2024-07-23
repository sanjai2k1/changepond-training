company = {'Infosys','ICICI bank','TCS','Bajaj'}
add_company = {'SBI','TATA consultancy','Infosys','TCS'}

union_method = company.union(add_company)
print('Union method will return all the element : ',union_method)

union_method = company | add_company
print('Using operator : ',union_method) 


intersection_method = company.intersection(add_company)
print('intersection ',intersection_method)
print()
difference_method = company.difference(add_company)
print('difference method :',difference_method)


symm_diference = company.symmetric_difference(add_company)
print('sym diiff',symm_diference)