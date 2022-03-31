class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
            We can't use an extra hashmap because space complexity has to be O(1).
            So let's use the given array as hashmap based on the logic that the all numbers are in the range of 1-n so we can use the index of array as the numbers (index+1 as 0th index will represent 1) keys of hashmap and the values as the number of occurrences of each number.
            We can achieve the above be decrementing each element by 1 to sustain the nth index as max value of array will be n but max index would be n-1.
            Now we will iterate over the array and will treat each element as the correct index of number.
            Everytime we encounter a number, the value at its correct index will be incremented by n.
            At the end we divide each number by n so that we get the count of each number(index of array) as the values of array.
            Now the elements with value == 2 would be the duplicates.
        """
        n = len(nums)
        nums = [num-1 for num in nums]
        print(nums)
        for num in nums:
            nums[num % n] += n
        # nums = [num//n for num in nums]
        output = []
        for key, num in enumerate(nums):
            if num//n == 2:
                output.append(key+1)
        return output
