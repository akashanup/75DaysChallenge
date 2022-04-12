# 206. Reverse Linked List

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

[![rev1ex1](rev1ex1.jpg)]()
### Example 1
```sh
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

[![rev1ex2](rev1ex2.jpg)]()
### Example 2
```sh
Input: head = [1,2]
Output: [2,1]
```

### Example 3
```sh
Input: head = []
Output: []
```

### Constraints
```sh
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
```

### Follow up
```sh
A linked list can be reversed either iteratively or recursively. Could you implement both?
```
