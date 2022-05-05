# Rat in a Maze

A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 

In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. 

Show the path by which a rat can reach to destination from source in a Maze.

[![ratinmaze_filled_path1](ratinmaze_filled_path1.png)]()
### Example 1
```sh
Input: 
    {1, 0, 0, 0}
    {1, 1, 0, 1}
    {0, 1, 0, 0}
    {1, 1, 1, 1}
Output: 
    {1, 0, 0, 0}
    {1, 1, 0, 0}
    {0, 1, 0, 0}
    {0, 1, 1, 1}
```
