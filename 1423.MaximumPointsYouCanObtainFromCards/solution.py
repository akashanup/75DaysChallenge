class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Take the k left most elements to start
        best = score = sum(cardPoints[:k])

        for i in range(1, k+1):

            # Lose an element from the left, add an element from the right
            score = score - cardPoints[k-i] + cardPoints[-i]
            best = score if score > best else best

        return best
