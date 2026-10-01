class Solution:
    def isValid(self, s: str) -> bool:
        #s='([{])'
        stack = []
        found = True
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if not stack:
                    found=False
                    break
                top = stack.pop()
                if top!='('and i==')':
                    found = False
                    break
                if top!='['and i==']':
                    found=False
                    break
                if top!='{'and i=='}':
                    found=False
                    break
        if stack:
            found = False
        return found


