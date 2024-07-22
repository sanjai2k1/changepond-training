class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
def constrct_tree(i,n,arr):
    root=None
    
    if i<n and arr[i] is not None:
        root=TreeNode(arr[i])
        root.left = constrct_tree(2*i+1,n,arr)
        root.right = constrct_tree(2*i+2,n,arr)
    return root

def find_path_from_root(node,data,arr):
    if node is None:
        return None
    if node==data:
        return arr
    arr.append("L")
    if find_path_from_root(node.left,data,arr):
        return arr
    arr.pop()
    arr.append("R")
    if find_path_from_root(node.right,data,arr):
        return arr
    arr.pop()

    
    
def find_leaves(node,arr):
    if node is None:
        return arr
    if node.left is None and node.right is None:
        arr.append(node)
    find_leaves(node.left,arr)
    find_leaves(node.right,arr)
    return arr


def display(node):
    if node is None:
        return
    print(node.val)
    display(node.left)
    display(node.right)
roots = [19,10,64,75,5,68,64,53,35,63,53,76,45,48,6,13,31,8,72,10,79,9,96,45,None,None,63,7,65,None,7,35,74,None,None,56,None,70,41,None,None,64,None,None,None,None,None,None,None,86,97,None,None,None,None,None,None,53,67,None,None,98,None,None,None,None,None,None,None,None,None,34,None,None,None,64,None,62]
root = constrct_tree(0,len(roots),roots)
# display(root)

distance = 1
leaves=find_leaves(root,[])
# leaves=list(set(leaves))
[print(i.val,end=" ") for i in leaves]
paths=[]
for i in leaves:
    paths.append(find_path_from_root(root,i,[]))
print(paths)
res=0

for i in range(0,len(paths)-1):
    for j in range(i+1,len(paths)):
        k=0
        while k<min(len(paths[i]),len(paths[j])):
            if paths[i][k] != paths[j][k]:
                break
            k+=1
        tot=len(paths[i][k:])+len(paths[j][k:])
        if tot<=distance:
            res+=1
print(res)