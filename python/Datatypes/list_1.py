#creating a list
course = ["Python",'Java','PHP']
rollno = [123,124,124]

#creating mixed type
mixed_type = ['Ketan',123,True,67,78]




print("accessing the values; ", mixed_type[-1])
print("accessing the values; ", mixed_type[-2])
print("accessing the values; ", mixed_type[-3])


print('Slicing : ',mixed_type[1:3])

print(mixed_type[:3])
print(mixed_type[-4:-1])



fruits=['Mango','Banana','Grapes','Watermelon']
fruits[1]='Kiwi'
print(fruits)


del fruits[3]
print(fruits)

fruits[-1] = 'Orange'

print(fruits)


nested_list = ['Shubham','Ketan',[21,22],[True,False]]
print(nested_list[0])
print(nested_list[1])
print(nested_list[2][0])
print(nested_list[2][1])
print(nested_list[3][0:2])

# create a tuple
student_id = (123,124,125,126)
ice_cream = ('vaniila','choco-chips','blueberry')

mixed_type = (123,'hello',False,56.78)
print("length of student id ",len(student_id))
print("length of student id ",ice_cream[2])
print("length of student id ",mixed_type[-2])
print("length of student id ",mixed_type[1:3])



# create a tuple
# homogenoius
student_id = (123,124,125,126)
ice_cream = ('Butterscotch', 'Choco-chips','Blueberry')
 
# heterogenious
mixed_type = (123,'Hello' , False , 56.78)
# len()
# using index ==> bluberry(postive index)
# using slicing ==> 'Hello',False
 

print("length of student id ",len(student_id))
print("value of positive index ",ice_cream[2])
print("value of negative index ",mixed_type[-2])
print("Slicing ",mixed_type[1:3])


ice_cream = ('vanilla')
print(ice_cream,type(ice_cream))
ice_cream=('vanilla',)
print(ice_cream,type(ice_cream))
# Create a tuple 
# Homogenus

student_id = (1,2,3,4,5,6)
ice_creame = ('Vanilla','Choco-chips','Blueberry')

# Hetrogenus
mixed_type = (123,'Hello',False,56.78)


print("length of student id ",len(student_id))
print("Blueberry",ice_creame[2])
print("False ",mixed_type[-2])
print("'Hello',False",mixed_type[1:3])


ice_creame = ('Vanilla')        # str
print(ice_creame,type(ice_creame))
ice_creame = ('Vanilla',)       # comma (tuple)
print(ice_creame,type(ice_creame))

# immutable
# mixed_type[0] = True
# print("False ",mixed_type)


ice_cream = ('vanilla','')
countmethod = ice_cream.count('vanilla')
print('count method:',countmethod)
print()
indexmethod = ice_cream.index('vanilla')
print('Index method',indexmethod)



student_name = "subham"
print('student name:',len(student_name))
#len 
#postive index :s
#negative index :b

print(len(student_name))
print(student_name[0])
print(student_name[-4])
#Slicing 
print(student_name[0:3])



nested_tuple = (['subham','ketan'],[21,22],(True,False))

print(nested_tuple[0])
print(nested_tuple[0][0])
print(nested_tuple[0][1])
print(nested_tuple[1])
print(nested_tuple[1][0])
print(nested_tuple[1][1])
print(nested_tuple[2])
print(nested_tuple[2][0])
print(nested_tuple[2][1])



