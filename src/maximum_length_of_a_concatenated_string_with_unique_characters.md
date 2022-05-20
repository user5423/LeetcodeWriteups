# Maximum Length of a Concatenated String with Unique Characters (Medium)

Problem URL: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# 

## Solution 1

Runtime: **123 ms**, faster than **70.54%** of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.

Memory Usage: **13.9 MB**, less than **88.78%** of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.

1. Preprocess the array
- Each string should have unique characters only - Therefore we remove strings with duplicate characters
- Duplicate array elements aren't removed as this is supported by the main body

2. Backtracking Solution

- Parameter options
	- `currentSolution` - This contains the set of characters concatenated so far
	- `currentLength` - This contains the length of the currentSolutionSet
	- `startIndex` - The start index tells the backtracking algorithm which elements that will be iterated over, and perform recursive calls on (if it satisfies a condition check stated below). The elements that can be iterated over are arr[startIndex:]
- Main Backtrcking Body
	- Base Case
		- Once there are no more base elements, we backtrack
	- For each available element (dictated by `startIndex`), the algorithm checks whether it has any common characters with `currentSolution`. 
	- If the array element has no common characters with `currentSolution`, then we perform a recursive call to `backtrackingSolution()`, with parameters:
		- `currentSolution` - combines the chars from the selected array element and the old `currentSolution`
		- `currentLength` - passes the length of the new `currentSolution`
		- `startIndex` - this is the increment of the selected array element + 1. This ensure that the backtracking recursive call doesn't try to add previously skipped/selected elements to `currentSolution`
	- If the array element has common characters with `currentSolution`
		- Then we backtrack
- Auxilliary Code
	- When creating a new `currentSolution` we update an object attribute if the `currentLength` is better than any previously found ones

**[Python Code Implementation](maximum_length_of_a_concatenated_string_with_unique_characters.py)**
