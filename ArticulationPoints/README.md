# Articulation Points

A vertex in an undirected connected graph is an articulation point (or cut vertex) if removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more components. They are useful for designing reliable networks. 

For a disconnected undirected graph, an articulation point is a vertex removing which increases number of connected components.

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
