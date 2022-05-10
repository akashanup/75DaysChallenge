class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product, curMax, curMin = -sys.maxsize, 1, 1

        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)

            product = max(product, curMax)

        return product

