# dp=[[30,25,16,7,8,9],[29,24,15,6,1,2],[28,23,14,5,4,3],
# [27,22,13,12,11,10],[26,21,20,19,18,17]]
# dp=[[1,2,3,4]]
rStart = 0
cStart = 0
WE = []
i,j=rStart,cStart
di=[0,1,0,-1]
dj=[1,0,-1,0]
rows=3
cols = 3
WEcheck=2
check=WEcheck
while i>=0 and j<cols and i<rows and j>=0:
    group = []
    k,l = i,j
    while  k>=0 and l<cols and k<rows and l>=0:
        group.append([k,l])
        k+=di[0]
        l+=dj[0]
        check-=1
        if check==0:
            break
    WEcheck+=2
    check=WEcheck
    i-=1
    j-=1
    WE.append(group)




i,j=rStart+1,cStart-1
EW=[]
EWcheck=4
check=EWcheck
print(i,j)
while i>=0 and j<cols and i<rows and j>=0:
    group = []
    k,l = i,j
    while  k>=0 and l<cols and k<rows and l>=0:
        group.append([k,l])
        k+=di[0]
        l+=dj[0]
        check-=1
        if check==0:
            break
        
    EWcheck+=2
    check=EWcheck
    i+=1
    j-=1
    EW.append(group[::-1])


i,j=rStart+1,cStart-1
SN=[]
SNcheck=4
check=SNcheck
while i>=0 and j<cols and i<rows and j>=0:
    group = []
    k,l = i,j
    while k>=0 and l<cols and k<rows and l>=0:
        group.append([k,l])
        k+=di[3]
        l+=dj[3]
        check-=1
        if check==0:
            break
    SNcheck+=2
    check=SNcheck
    if i==rows-1:
        j-=1
    else:
        i+=1
        j-=1
    SN.append(group)


i,j=rStart,cStart+1
NS=[]
NScheck=2
check=NScheck
while i>=0 and j<cols and i<rows and j>=0:
    group = []
    k,l = i,j
    while k>=0 and l<cols and k<rows and l>=0:
        group.append([k,l])
        k+=di[1]
        l+=dj[1]
        check-=1
        if check==0:
            break
    NScheck+=2
    check=NScheck
    if i==0:
        j+=1
    else:
        i-=1
        j+=1
    NS.append(group)


print(WE)
print(NS)
print(EW)
print(SN)


# res=[]
# while WE or NS or EW or SN:
#     if not res:
#         if WE:
#             res.append(WE[0][0])
#         elif NS:
#             res.append(NS[0][0])
#         elif EW:
#             res.append(EW[0][0])
#         elif SN:
#             res.append(SN[0][0])
#     else:
#         if WE:
#             poped=WE[0]
#             for m in poped:
#                 if not (res[-1][0]== m[0] and res[-1][1]==m[1]):
#                     res.append(m)
#             WE.pop(0)
#         if NS:
#             poped=NS[0]
#             NS.pop(0)
#             for m in poped:
#                 if not (res[-1][0]== m[0] and res[-1][1]==m[1]):
#                     res.append(m)
            
#         if EW:
#             poped=EW[0]
#             EW.pop(0)
#             for m in poped:
#                 if not (res[-1][0]== m[0] and res[-1][1]==m[1]):
#                     res.append(m)    
#         if SN:
#             poped=SN[0]
#             SN.pop(0)
#             for m in poped:
#                 if not (res[-1][0]== m[0] and res[-1][1]==m[1]):
#                     res.append(m)

# print(res)
# ans=list(map(lambda x : x[1],res))
            
# print(ans)