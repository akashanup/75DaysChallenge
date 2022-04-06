# 852. Peak Index in a Mountain Array

Let's call an array arr a mountain if the following properties hold:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  - arr[0] < arr[1] < ... arr[i-1] < arr[i]
  - arr[i] > arr[i+1] > ... > arr[arr.length - 1]
  
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

### Example 1
```sh
Input: arr = [0,1,0]
Output: 1
```

### Example 2
```sh
Input: arr = [0,2,1,0]
Output: 1
```

### Example 3
```sh
Input: arr = [0,10,5,2]
Output: 1
```

### Constraints
```sh
3 <= arr.length <= 10^4
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.
```

### Follow Up
```sh
Finding the O(n) is straightforward, could you find an O(log(n)) solution?
```
