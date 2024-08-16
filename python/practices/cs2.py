def solve(ind,n,candidates,target,arr,ans):
    if target==0:
        print(arr)
        # ans.add(tuple(arr))
        return
    for i in range(ind,n):
        if i> ind and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
                break
        arr.append(candidates[i])
        solve(i+1,n,candidates,target-candidates[i],arr,ans)
        arr.pop()
    
     
    







candidates =[10,1,2,7,6,1,5]
target = 8
candidates.sort()
ans=set()
arr=[]
solve(0,len(candidates),candidates,target,arr,ans)
ans= list(map(lambda x : list(x),ans))
print(ans)