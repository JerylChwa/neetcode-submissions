class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mappings = {')':'(', '}':'{', ']':'['}
        
        for char in s:
            if char in mappings.values():
                stack.append(char)
            elif char in mappings.keys():
                if not stack or stack[-1] != mappings[char]:
                    return False
                else:
                    stack.pop(-1)
      
        
        if len(stack) != 0:
            return False
        
        return True