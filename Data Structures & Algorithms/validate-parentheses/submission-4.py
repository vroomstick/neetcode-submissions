class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c not in brackets:
                stack.append(c)

            else:
                if len(stack) != 0 and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            

        return True if len(stack) == 0 else False

        