# from collections import deque
# def is_balanced(not_balanced):
#     if 'a' not in not_balanced or 'b' not in not_balanced:
#         return True
#     balanced_a_first=True 
#     for i in range(len(not_balanced)):
#         if not_balanced[i]=='a':
#             if 'b' in not_balanced[:i]:
#                 balanced_a_first=False
#                 break
#     return balanced_a_first 
# s = "aababbab"
# not_balanced = list(s)
# queue = deque()
# if not is_balanced(not_balanced):
#     queue.append((not_balanced,0))
# print(queue)
# # while queue:
# poped = queue.popleft()
# if not is_balanced(poped[0]):
#     checkstr=poped[0][:]
#     chckcnt=poped[1]
#     while 'a' in checkstr[checkstr.index('b')+1:]:
#         checkstr.pop(checkstr.index('b')+checkstr[checkstr.index('b')+1:].index('a'))
#         chckcnt+=1
#         print(checkstr,"h2")
#         if is_balanced(checkstr):
#             break
#     queue.append((checkstr,chckcnt))
#     checkstr=poped[0][:]
#     chckcnt=poped[1]
#     while 'a' in checkstr[checkstr.index('a')+1:]:
#         checkstr.pop(checkstr.index('a')+checkstr[checkstr.index('a')+1:].index('b'))
#         chckcnt+=1
#         print(checkstr,"hii")
#         if is_balanced(checkstr):
#             break
#     queue.append((checkstr,chckcnt))
    
    
    # for i in range(len(poped[0])):
        # if poped[0][i]=='a' and 'b' in poped[0][:i]:
        #     new_str=poped[0][:]
        #     new_str.pop(i-poped[0][:i].index('b'))
        #     queue.append((new_str,poped[1]+1))
        # if poped[0][i]=='a' and 'b' in poped[0][i+1:]:
        #     new_str=poped[0][:]
        #     new_str.pop(i+poped[0][i+1:].index('b'))
        #     queue.append((new_str,poped[1]+1))
    # for i in range(len(poped[0])):
    #     if poped[0][i]=='b' and 'a' in poped[0][:i]:
    #         new_str=poped[0][:]
    #         new_str.pop(i-poped[0][:i].index('a'))
    #         queue.append((new_str,poped[1]+1))
        # if poped[0][i]=='b' and 'a' in poped[0][i+1:]:
        #     new_str=poped[0][:]
        #     new_str.pop(i+poped[0][i+1:].index('a'))
        #     queue.append((new_str,poped[1]+1))
# else:
#     print(poped)
#     break
# print(queue)

# import sys
# def is_balanced(not_balanced):
#     if 'a' not in not_balanced or 'b' not in not_balanced:
#         return True
#     balanced_a_first=True 
#     for i in range(len(not_balanced)):
#         if not_balanced[i]=='a':
#             if 'b' in not_balanced[:i]:
#                 balanced_a_first=False
#                 break
    
#     balanced_b_first=True 
#     for i in range(len(not_balanced)):
#         if not_balanced[i]=='b':
#             if 'a' in not_balanced[:i]:
#                 balanced_b_first=False
#                 break
#     return balanced_a_first or balanced_b_first
# def solve(ind,n,arr,lst,ans,dp):
#     if ind==n:
#         if is_balanced(arr):
#             print(arr)
#             ans[0]=min(ans[0],len(lst)-len(arr))
#             dp[ind]=ans[0]
#         return ans[0]
#     if dp[ind]!=10**9:
#         return dp[ind]
#     arr.append(lst[ind])
#     left=solve(ind+1,n,arr,lst,ans,dp)
#     arr.pop()
#     right=solve(ind+1,n,arr,lst,ans,dp)
#     dp[ind]=min(dp[ind],min(left,right))
#     return dp[ind]
           
# s="bbaaaaabb"
# lst=list(s)
# ans=[10**9]
# dp=[[10**9 ] for j in range(len(s)+1)]
# # print(dp)
# print(solve(0,len(s),[],lst,ans,dp))
# [print(i) for i in dp]
# # print(ans)



def is_balanced(not_balanced):
    if 'a' not in not_balanced or 'b' not in not_balanced:
        return True
    balanced_a_first=True 
    for i in range(len(not_balanced)):
        if not_balanced[i]=='a':
            if 'b' in not_balanced[:i]:
                balanced_a_first=False
                break
    return balanced_a_first 



def solve(ind,n,arr,lst,ans,prev):
    if ind==n:
        print(arr)
        return
    print(arr)
    if prev==-1 and lst[ind]=='a' or prev=='a' and lst[ind]=='a':
        
        arr.append('a')
        
        solve(ind+1,n,arr,lst,ans,'a')
        arr.pop()
    elif prev=='a' and lst[ind]=='b':
        arr.append('b')
        solve(ind+1,n,arr,lst,ans,'b')
        arr.pop()
        solve(ind+1,n,arr,lst,ans,'a')
    elif prev=='b' and lst[ind]=='b':
        arr.append('b')
        solve(ind+1,n,arr,lst,ans,'b')
        arr.pop()
    elif prev == 'b' and lst[ind]=='a':
        solve(ind+1,n,arr,lst,ans,'b')
        
        
        

        
        
        


s = "aababbab"

cnt=0
lst=list(s)
ans=[0]
n=len(s)
if not  is_balanced(s):
    solve(0,n,[],lst,ans,-1)