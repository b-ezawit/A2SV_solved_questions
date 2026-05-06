# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorderSuccessor(node):
            if not node:
                return None
            current = node
            while current.left:
                current = current.left
            return current
        
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            #if key == root.val

            #1. if no right subtree
            if not root.right:
                return root.left
            
            #2. if no left subtree
            elif not root.left:
                return root.right

            #3. if both children exist
            else:
                inorder_suc = inorderSuccessor(root.right)      
                if inorder_suc:
                    root.val = inorder_suc.val
                    root.right = self.deleteNode(root.right,root.val)
                else:
                    root  = inorder_suc

    
        return root      


        


        