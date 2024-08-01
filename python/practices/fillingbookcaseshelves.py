# def solve(ind,books,shelfwidth,n,arr,prev,w,ans):
#     if ind==n or prev==n:
#         height=0
        
#         for i in arr:
#             h=0
#             for j in i:
#                 h=max(h,books[j][1])
#             height+=h
#         print(arr,height,"hii")
#         ans[0]=min(ans[0],height)
#         return 
#     print(ind,books[ind][0],shelfwidth,arr)
    
#     if prev==-1 and books[ind][0]<=shelfwidth:
        
#         arr[ind].append(ind)
#         solve(ind+1,books,shelfwidth-books[ind][0],n,arr,0,w,ans)
#         arr[ind].pop()

#     else:
#         if books[ind][0]<=shelfwidth:
#             # print(ind,books[ind][0],shelfwidth)
#             arr[prev].append(ind)
#             solve(ind+1,books,shelfwidth-books[ind][0],n,arr,prev,w,ans)
#             arr[prev].pop()
#             arr[prev+1].append(ind)
#             solve(ind+1,books,w,n,arr,prev+1,w,ans)
#             arr[prev+1].pop()
#         else:
#             arr[ind+1].append(ind)
#             solve(ind+1,books,w,n,arr,prev+1,w,ans)
#             arr[ind+1].pop()

# books = [[7,3],[8,7],[2,7],[2,5]]
# shelfWidth = 10
# n=len(books)
# arr=[[]for i in range(n+1)]
# ans=[10**9]
# solve(0,books,shelfWidth,n,arr,-1,shelfWidth,ans)
# print(ans[0])

books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelfWidth = 4
shelves=[]

dp=[[-1 for j in range(len(books))]for i in range(len(books))]

for i in range(0,len(books)):
    dp[i][i]=books[i][0]

# [print(i) for i in dp]
ind=0
for i in range(0,len(books)):
    w=shelfWidth
    w=shelfWidth-books[i][0]
    # print(w)
    for j in range(i+1,len(books)):
        if books[j][0]<=w:
            dp[i][j]=books[j][0]
            w-=books[j][0]
        else:
            break
    else:
        break
    ind+=1
    
print(ind)

for i in range(0,ind+1):
    for j in range(len(books)):
        if dp[i][j]==-1:
            break
        else:
            
            
        
    

[print(i) for i in dp]

