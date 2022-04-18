class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        nextSmaller = [-1] * n
        stack = [-1]
        for i in range(n-1, -1, -1):
            while stack[-1] >= arr[i]:
                stack.pop()
            nextSmaller[i] = stack[-1]
            stack.append(arr[i])
        return nextSmaller
