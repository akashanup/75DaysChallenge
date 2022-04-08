"""
Logic:
    If you have a single sorted array you can easily calculate the median by considering the middle element(s).
    If we deep dive the above statement we can figure out that the array could be partitioned into two parts where the lengths of two part differs by at max 1.
    For example, Let's say the array is [1,2,3,4,5,6,7,8]
        Partitioned into two parts: l=>[1,2,3,4]  and  r=>[5,6,7,8]
    OR If the array is [1,2,3,4,5,6,7]
        Partitioned into two parts: l=>[1,2,3,4]  and  r=>[5,6,7]
    Now the median would be,
        1. If l and r of same length then, median = max(l)+min(r) / 2
        2. If l ard r differs by 1 length then, median = max(l)
    Now to calculate the median of two sorted arrays, assume the two arrays are merged and still sorted.
    Then the length of merged array would be m+n, and it can be partitioned into two at (m+n / 2)th index or the index at half of length of merged array.
    Now the question arises as how to partition the assumed merged sorted array?
    Since we know the partition index(half), we can calculate how many values will be on the left part and right part of array.
    For example,
        arr1 => [1,4,5,8,10], m = 5
        arr2 => [2,3,9], n = 3
        Assume the above arrays are merged and sorted, therefore the array would be,
            [1,2,3,4,5,8,9,10], m+n = 8
        Now the array could be partitioned into two parts of length 4 (4 elements will be in left part and 4 will be in right part).
    Now the question arises, which of the 4 elements would lie in the left part and which 4 will lie in right.
    Let's say l1 be the part of arr1 and l2 would be the part of arr2 which would lie on the left part of merged array.
    Similarly, r1 and r2 would lie in the right part of sorted array.
    So, l1+l2 = 4 and r1+r2 = 4
    Now l1 can be determined by iterating the first array for first 4 elements and for each element, we can check the corresponding values of l2 as l1+l2 == 4.
    For example, if,
        1. l1 => [1,4,5,8] then l2 would be []
        2. l1 => [1,4,5] then l2 would be [2]
        3. l1 => [1,4] then l2 would be [2,3]
        4. l1 => [1] then l2 would be [2,3,9]
        5. l1 => [] then l2 would be [2,3,9] NOT POSSIBLE because l1+l2 should be equal to 4
    Similarly, we can calculate r1 and r2.
    The above is a demonstration of linear search. Since our both arrays are sorted, we could use Binary search for optimal solution.
    Now the correct combination of l1,l2,r1 and r2 would be such that,
        max(l1) <= min(r2) and max(l2) <= min(r1) i.e,
        l1 => [1,4], r1 => [5,8,10]
        l2 => [2,3], r2 => [9]
    And median would be, max(max(l1), max(l2)) + min(min(r1),min(r2)) / 2
    Or If m+n is odd then median would be, max(max(l1), max(l2))
"""


import sys


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        # To handle edge cases
        if n < m:
            return self.findMedianSortedArrays(nums2, nums1)
        half = (m+n+1) // 2

        # Find the partition indexes by binary search for both the arrays
        start, end = 0, m
        while start <= end:
            partition1 = start + ((end-start)//2)
            partition2 = half-partition1

            # Left and Right values at the partition index for both the arrays
            l1 = -sys.maxsize if partition1 == 0 else nums1[partition1-1]
            l2 = -sys.maxsize if partition2 == 0 else nums2[partition2-1]
            r1 = sys.maxsize if partition1 == m else nums1[partition1]
            r2 = sys.maxsize if partition2 == n else nums2[partition2]

            if l1 <= r2 and l2 <= r1:
                # Partition indexes found!
                if (m+n) & 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1, r2)) / 2
            else:
                if l1 > r2:
                    end = partition1-1
                else:
                    start = partition1+1
        return 0.0
