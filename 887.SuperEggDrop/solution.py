import sys

"""
    Logic:
        1. For any floor i, dropping an egg from this floor would always lead to two possibilities-
            a. The egg would break.
                i. It means, floors greater than ith floor are of no use as the egg would definitely break for all floors (>i).
            b. The egg would not break.
                i. It means, floors smaller that ith floor are of no use as the egg would never break for all floors (<=i).
        2. Let's say we have n floors and k eggs and we want to know the minimum number of moves by which we can assure that an egg when dropped from a floor f will never break. Let's denote it as dp(n, k).
        3. From step 1, we can deduce that-
            a. dp(n,k) = min(1+ max(dp(i-1, k-1), dp(n-i, k))) for all i in [1,n]
                i. For floor i, max(dp(i-1, k-1), dp(n-i, k))) is used because we want to find the maximum cases that could arise as then only we can guarantee the value of floor f
                ii. min(1+ max(dp(i-1, k-1), dp(n-i, k))) for all i in [1,n] is used because we want to find the minimum number of moves that is done for all floors [1,n] guarantee the value of floor f.        
"""


class Solution:
    def dp(self, n, eggs, lookup):
        key = (n, eggs)
        if key not in lookup:
            if n == 0 or n == 1:
                lookup[key] = n
            elif eggs == 1:
                lookup[key] = n
            else:
                minMoves = sys.maxsize
                """
                    Since 1->n would be always sorted, so we can use binary search instead of linear search to solve this optimally.
                        for i in range(1, n+1):
                            survived = self.dp(n-i, eggs, lookup)
                            notSurvived = self.dp(i-1, eggs-1, lookup)
                            minMoves = min(minMoves, 1+max(survived, notSurvived))
                        lookup[key] = minMoves
                """
                bottom, top = 1, n
                while bottom < top:
                    mid = bottom + ((top - bottom) // 2)
                    survived = self.dp(n - mid, eggs, lookup)
                    notSurvived = self.dp(mid - 1, eggs - 1, lookup)
                    # If egg survived at (mid)th floor then check whether the egg could survive at (mid+1)th floor
                    if survived > notSurvived:
                        bottom = mid + 1
                    else:
                        # If egg didn't survive at (mid)th floor then check for below floors
                        top = mid
                    # moves would be 1 + maximum of survived, notSurvived for remaining of floors and eggs.
                    moves = 1 + max(survived, notSurvived)

                    minMoves = min(minMoves, moves)

                lookup[key] = minMoves

        return lookup[key]

    def superEggDrop(self, k: int, n: int) -> int:
        return self.dp(n, k, {})
