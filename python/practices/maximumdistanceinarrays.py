arrays = [[1,5],[3,4]]
maxes = []
mins=[]
for i in range(len(arrays)):
    maxes.append((max(arrays[i]),i))
    mins.append((min(arrays[i]),i))
# ans.sort()
ans=-float('inf')
maxes.sort(key=lambda x : -x[0])
mins.sort(key=lambda x : x[0])
print(maxes)
print(mins)
# for i in maxes:
#     for j in mins:
#         if i[1]!=j[1]:
#             ans=max(ans,abs(i[0]-j[0]))
for j in maxes:
    maxi=j
    for i in mins:
        if i[1]!=maxi[1]:
            ans=max(ans,maxi[0]-i[0])
            break
print(ans)


    