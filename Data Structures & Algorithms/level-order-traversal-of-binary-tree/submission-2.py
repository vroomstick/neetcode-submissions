# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bfs(root):
            queue = deque()

            if not root:
                return []

            if root:
                queue.append(root)

            level = 0
            result = []

            while len(queue) > 0:
                current = []
                for i in range(len(queue)):
                    curr = queue.popleft()
                    current.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

                level = level + 1
                result.append(current)

            return result

        return bfs(root)