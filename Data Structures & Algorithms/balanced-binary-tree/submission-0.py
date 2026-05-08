# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def postdfs(node):
            if not node:
                return 0
            left, right = postdfs(node.left), postdfs(node.right)
            height = max(right, left) + 1
            if left == -1:
                return -1
            if right == -1:
                return -1
            if abs(left - right) <= 1:
                return height
            else:
                return -1

            
            

        return postdfs(root) != -1

        


        