# 206. Reverse Linked List


You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

### Example 1
```sh
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

### Example 2
```sh
Input: nums = [-1]
Output: [0]
```

### Example 3
```sh
Input: nums = [-1,-1]
Output: [0,0]
```

### Constraints
```sh
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
```

### Follow up
```sh
A linked list can be reversed either iteratively or recursively. Could you implement both?
```
