nums = [-1,1,-6,4,5,-6,1,4,1]
maps = {}
for i in nums:
    maps[i]=nums.count(i)
values= sorted(set(maps.values()))
# print(values)
# print(maps)
keys_with_value = [sorted([key for key, value in maps.items() if value == i],reverse=True) for i in values]
# print(keys_with_value)
res=[]
for i in keys_with_value:
    for j in i:
        res+=[j]*maps[j]
print(res)
