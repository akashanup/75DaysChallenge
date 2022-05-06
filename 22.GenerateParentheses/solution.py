class Solution:
    def isValid(self, parenthesis):
        score = 0
        for i in parenthesis:
            if i == '(':
                score += 1
            else:
                score -= 1
            if score < 0:
                return False
        return score == 0

    def dpFn(self, n, parenthesis, lookup):
        if len(parenthesis) == n * 2:
            lookup.append(parenthesis)
        else:
            self.dpFn(n, parenthesis + ')', lookup)
            self.dpFn(n, parenthesis + '(', lookup)
    
    def generateParenthesis(self, n: int) -> List[str]:
        lookup = []
        # Get all possible combinations
        self.dpFn(n, '', lookup)
        # Remove duplicates
        lookup = {i for i in lookup}
        # Filter the valid parentheses combinations
        lookup = [i for i in lookup if self.isValid(i)]
        return lookup
