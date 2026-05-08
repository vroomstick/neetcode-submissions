# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        single, double = head, head
        # if single and double ever meet it is a cycle, 
        #if double ever meets a node with a pointer to NULL then return False
        while double and double.next:
            single = single.next
            double = double.next.next
            if single == double:
                return True
        

        return False

        