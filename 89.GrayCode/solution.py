class Solution:
    def grayCode(self, n: int) -> List[int]:
        code = [['0', '1']]
        for i in range(1, n):
            '''
                greycode(n) = ("0" * result of greycode(n-1)) + ("1" * reverse of result of grecode(n-1))
                For example:
                greycode(1) = ["0", "1"] => Known Base Case
                greycode(2) = ["0"+"0", "0"+"1"] + ["1"+"1", "1"+"0"]
                            = ["00", "01", "11", "10"]
                Now extrapolate the above logic.
            '''
            code.append([("0" + _) for _ in code[i - 1]] + [("1" + _) for _ in code[i - 1][::-1]])
        return [int(i, 2) for i in code[n-1]]
