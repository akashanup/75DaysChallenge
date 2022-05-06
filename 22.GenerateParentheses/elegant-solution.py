class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        i = 1
        # Base case
        validI = {"()"}
        while i < n:
            temp = set()
            """
                For every pair, for all the possible combinations, try to insert '()' and save it to 'temp' set so that all combinations are unique.
            """
            for combination in validI:
                for j in range(len(combination) + 1):
                    temp.add(combination[:j] + "()" + combination[j:])
            i += 1
            validI = temp

        return validI
