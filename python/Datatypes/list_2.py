country = ['india','south korea','iran','japan','turkey','iraq']





for name in country:
    print(f'{name.title()}, these are the list of countries')


author_name =(' jk rowling','rachel aaron','hans aanrud','verna aardema')

for author in author_name:
    print(f'{author.title()}, these are the list of authors')


for auth_name in range(len(author_name)):
    print(author_name[auth_name],'------------',auth_name)


time_update = "it's 4.15 pm"
for i in range(len(time_update)):
    print(time_update[i])
