new_list = [i for i in range(1,11)]
print('list comprehension :',new_list)

new_list = [i for i in range(1,11) if i%2==0]
print('list comphrehension : ',new_list)

vowels = ['a','e','i','o','u']
name="sanjai"
withoutvowels = [i for i in name if i not in vowels]
print(withoutvowels)