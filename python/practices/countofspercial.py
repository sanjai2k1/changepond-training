import math
l=5
r=7

# dp=[0 for i in range(r+1)]

# for i in range(1,r+1):
#     cnt=0
#     for j in range(i):
#         if dp[j]==0:
#             if j!=0 and j!=i:
#                 if i%j==0:
#                     cnt+=1
#             dp[i]=cnt
#         elif j!=0 and j!=i:
#             if i%j==0:
#                 cnt+=dp[j]
#                 dp[i]=cnt
# ans=len(dp[l:])-(dp[l:].count(2))
# print(ans)

cnt=0
for i in range(int(math.sqrt( l)),int(math.sqrt(r))+1):
    if i!=2 and i%2==0:
        continue
    else:
        isprime=0
        for j in range(1,i//2 +1):
            if i%j==0:
                isprime+=1
        if isprime:
            cnt+=1
        # print(i,isprime)
print(cnt)
            
tot=int(math.sqrt(r))-int(math.sqrt( l))
print(r-l-cnt+1)