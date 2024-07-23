Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'rolex':8000
}

key_method = Watch_details.keys()
print('keys',key_method)

value_method = Watch_details.values()
print(value_method)




get_method =  Watch_details.get('titan')
print('get' ,get_method)

Watch_details.update({'Noise':12000})
print('update ',Watch_details)


Watch_details.pop('titan')
print('pop method :' ,Watch_details)

