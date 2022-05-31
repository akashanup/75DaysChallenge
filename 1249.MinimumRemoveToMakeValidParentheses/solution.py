class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        close = s.count(')')
        closeUsed = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ('(', ')'):
                if s[i] == ')':
                    # If there are any open '(' i.e, open > 0 then use the current ')' to close it.
                    # Else open <= 0 then remove the current ')'
                    if open > 0:
                        # A pair is found.
                        stack.append(s[i])
                        open -= 1
                    else:
                        closeUsed += 1
                else:
                    # If the current '(' can be mapped to further ')' then map it.
                    # Else (close - closeUsed <= 0) then remove the current '(' as its corresponding pair will not be found.
                    if close - closeUsed > 0:
                        # A pair will be found.
                        stack.append(s[i])
                        open += 1
                        closeUsed += 1
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
