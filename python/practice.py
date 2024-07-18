class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i]) if arr[i] is not None else None
        root = temp
    if root is not None:
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

def find_leaves(node, arr):
    if node is None:
        return
    if node.left is None and node.right is None:
        arr.append(node.val)
    find_leaves(node.left, arr)
    find_leaves(node.right, arr)

# Given list
arr = [19,10,64,75,5,68,64,53,35,63,53,76,45,48,6,13,31,8,72,10,79,9,96,45,None,None,63,7,65,None,7,35,74,None,None,56,None,70,41,None,None,64,None,None,None,None,None,None,None,86,97,None,None,None,None,None,None,53,67,None,None,98,None,None,None,None,None,None,None,None,None,34,None,None,None,64,None,62]

# Construct the binary tree
root = insert_level_order(arr, None, 0, len(arr))

# Find the leaves
leaves = []
find_leaves(root, leaves)
print(leaves)