# 4Sum (Medium)

Problem URL: https://leetcode.com/problems/4sum/

#

## Solution 1

Runtime: **1098 ms**, faster than **57.76%** of Python3 online submissions for 4Sum.

Memory Usage: **13.9 MB**, less than **93.95%** of Python3 online submissions for 4Sum.

### Implementation

Uses a nested for loop, where on each iteration, there is a right and left boundary element. For each iteration, we use the right and left boundary and perform two-pointer algorithm on the array on the range arr[left+1:right].

If `leftBoundary` + `left` + `right` + `rightBoundary` is equal to the target, then we add the solution to the set of solutions

This has a time complexity of **O(n^3)** and a space complexity of **O(n)**

**[Python Code Implementation](4Sum.py)**

## Solution 2

Using a hashmap, we can reduce the time complexity to **O(n^2)** at the cost of increasing the space complexity to **O(n^2)**. *TODO*: Implement this
