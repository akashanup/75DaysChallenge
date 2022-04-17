class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] in ")]}":
                if len(stack) and ((s[i] == ")" and stack[-1] == "(") or (s[i] == "]" and stack[-1] == "[") or (s[i] == "}" and stack[-1] == "{")):
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
