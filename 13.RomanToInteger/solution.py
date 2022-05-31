class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i = len(s)-1
        while i >= 0:
            if s[i] == 'I':
                num += 1
            elif s[i] == 'V':
                if i > 0 and s[i-1] == 'I':
                    num += 4
                    i-= 1
                else:
                    num += 5
            elif s[i] == 'X':
                if i > 0 and s[i-1] == 'I':
                    num += 9
                    i-= 1
                else:
                    num += 10
            elif s[i] == 'L':
                if i > 0 and s[i-1] == 'X':
                    num += 40
                    i-= 1
                else:
                    num += 50
            elif s[i] == 'C':
                if i > 0 and s[i-1] == 'X':
                    num += 90
                    i-= 1
                else:
                    num += 100
            elif s[i] == 'D':
                if i > 0 and s[i-1] == 'C':
                    num += 400
                    i-= 1
                else:
                    num += 500
            elif s[i] == 'M':
                if i > 0 and s[i-1] == 'C':
                    num += 900
                    i-= 1
                else:
                    num += 1000
            i -= 1
        return num
