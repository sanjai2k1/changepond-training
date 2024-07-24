# def comp(x,y):
#     if x[1]!=y[1]:
#         return x[1]-y[1]
#     return x[2]-y[2]
# mapping = [0,1,2,3,4,5,6,7,8,9]
# nums = [789,456,123]
 
# maps={}

# for i in range(0,len(mapping)):
#     maps[i]=mapping[i]
# res=[]
# cnt=0
# for j in nums:
#     arr=[]
#     for i in str(j):
#         arr.append(str(maps[int(i)]))
#     res.append((j,int("".join(arr)),cnt))
#     cnt+=1
# fin = sorted(res, key = comp)
# ans=[i[0] for i in fin]
# print(ans)
    
from functools import cmp_to_key

def comp(x, y):
    if x[1] != y[1]:
        return x[1] - y[1]
    return x[2] - y[2]

mapping = [5,6,8,7,4,0,3,1,9,2]
nums = [7686,97012948,84234023,2212638,99]

maps = {i: mapping[i] for i in range(len(mapping))}

res = []
cnt = 0
for j in nums:
    arr = []
    for i in str(j):
        arr.append(str(maps[int(i)]))
    res.append((j, int("".join(arr)), cnt))
    cnt += 1

fin = sorted(res, key=cmp_to_key(comp))
ans = [i[0] for i in fin]
print(ans)