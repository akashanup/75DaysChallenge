# Activity Selection

Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day.

### Example 1
```sh
Input: N = 2, start[] = {2, 1}, end[] = {2, 2}
Output: 1
Explanation: A person can perform only one of the given activities.
```

### Example 2
```sh
Input: N = 4, start[] = {1, 3, 2, 5}, end[] = {2, 4, 3, 6}
Output: 3
Explanation: A person can perform activities 1, 2 and 4.
```

### Task
```sh
You don't need to read input or print anything. Your task is to complete the function activityselection() which takes array start[ ], array end[ ] and integer N as input parameters and returns the maximum number of activities that can be done.
```

### Constraints
```sh
1 <= N <= 2*10^5
1 <= start[i] <= end[i] <= 10^9
```
