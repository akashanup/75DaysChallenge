class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow

