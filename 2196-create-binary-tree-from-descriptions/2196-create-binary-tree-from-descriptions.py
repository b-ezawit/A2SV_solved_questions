# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = {}
        root = 0
        for par,child,isLeft in descriptions:
            children[child] = 1
        
        for par,child,isLeft in descriptions:
            if par not in children:
                root = par
                break
        
        node = {}
        for par,child,isLeft in descriptions:
            if par not in node:
                node[par] = TreeNode(val=par,left=None,right=None)
            if child not in node:
                node[child] = TreeNode(val=child,left=None,right=None)

            if isLeft:
                node[par].left = node[child]
            else:
                node[par].right = node[child]
        
        return node[root]
