def solveasc(ind,n,rating,arr,ans,prev,dp):
    if ind==n:
        print(arr)
        if len(arr)==3:
            asce=True
            for i in range(0,2):
                if arr[i]>arr[i+1]:
                    asce=False
                    break
            if asce:
                ans[0]+=1
                return ans[0]
            return 0
        return 0 
    # if dp[ind][prev+1]!=-1:
    #     return dp[ind][prev+1]
    pick=0
    notpick=0
    if prev == -1 or rating[ind]>prev:
        arr.append(rating[ind])
        pick=solveasc(ind+1,n,rating,arr,ans,rating[ind],dp)
        arr.pop()
    notpick=solveasc(ind+1,n,rating,arr,ans,prev,dp)
    dp[ind][prev]=min(pick+notpick,0)
    return pick+notpick

def solvedsc(ind,n,rating,arr,ans,prev):
    if ind==n:
        print(arr)
        if len(arr)==3:
            dsce=True
            for i in range(0,2):
                if arr[i]<arr[i+1]:
                    dsce=False
                    break
            if dsce:
                ans[0]+=1
                return ans[0]
            return 0
        return 0 
    if prev == -1 or rating[ind]<prev:
        arr.append(rating[ind])
        solvedsc(ind+1,n,rating,arr,ans,rating[ind])
        arr.pop()
    solvedsc(ind+1,n,rating,arr,ans,prev)

rating = [2,5,3,4,1]
n=len(rating)
dp=[[-1 for j in range(max(rating)+1)]for i in range(max(rating)+1)]
ans=[0]
# print(new)
arr=[]
solveasc(0,n,rating,arr,ans,-1,dp)
print(ans[0],"ans")
[print(i) for i in dp]
print(dp[0][0],"dp")
# ans=[0]
# dp=[[-1 for j in range(n+2)]for i in range(n+2)]
# dsc=solvedsc(0,n,rating,[],ans,-1)
# solve(0,n,new,[])
print(ans[0],"ans")
# print(asc+dsc)