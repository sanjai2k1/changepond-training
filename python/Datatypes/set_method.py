mixed_type = {'subham',25,124,True}
more_add = {'rahul',24}

mixed_type.add('trainer')
print('add ',mixed_type)
# update() method
mixed_type.update(more_add)
print(mixed_type)

# discard() method -> remove Specifi element
mixed_type.discard(True)
print(mixed_type)
mixed_type.discard('hello')
# remove() method
mixed_type.remove(25)
print(mixed_type)