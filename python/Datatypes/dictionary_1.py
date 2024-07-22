Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'titan':3000
}

print('watch details',Watch_details)  # titan (consider the latest key value)
print(len(Watch_details))
print(type(Watch_details))
print('using key' ,Watch_details['titan'])

Watch_details={
    'titan':8000,
    'fastrack':5000,
    'casio':10000,
    'rolex':8000
}


print('watch details',Watch_details)  
print(len(Watch_details))
print(type(Watch_details))
print('using key' ,Watch_details['titan'])
print('using key' ,Watch_details['rolex'])
Watch_details['omega'] = 4000
print('watch details',Watch_details)  
Watch_details['IWC'] =  5000
print('watch details',Watch_details)  

foods ={'idly':100,
        'pongal':200}

print("before adding",foods)
foods['dosa']=300
print("after adding : ",foods)
foods['dosa']=400
print("after modifying ",foods)


users={
    'kastubag':{
        'firstname':'kasturi',
        'lastname':'Chaware',
        'Location':'Pune'
    },
    'shrebag':{
        'firstname':'Shreya',
        'lastname':'Badge',
        'Location':'Nagpur'
    },
    'prajbag':{
        'firstname':'Prajakta',
        'lastname':'Patil',
        'Location':'Chennai'
    }
}

for i in users:
    print(f'firstname : {users[i]['firstname']} lastname : {users[i]['lastname']} Location : {users[i]['Location']}')

print(users['kastubag']['firstname'])
print(users['prajbag'].get('Location'))










