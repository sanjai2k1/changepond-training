def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else :
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def meger_partion(nums):
    if len(nums)<=1:
        return nums
    
    mid=len(nums)//2
    left = meger_partion(nums[:mid])
    right=meger_partion(nums[mid:])
    return merge(left,right)
    
    




nums = [5,2,3,1]
print(meger_partion(nums))