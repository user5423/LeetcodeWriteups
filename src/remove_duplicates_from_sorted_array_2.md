# Maximum Length of a Concatenated String with Unique Characters (Medium)

Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# 

## Solution 1

Runtime: **63 ms**, faster than **69.86%** of Python3 online submissions for Remove Duplicates from Sorted Array II.

Memory Usage: **13.9 MB**, less than **75.88%** of Python3 online submissions for Remove Duplicates from Sorted Array II.

### Implementation

This approach consists of two passes of the array. The constraints of the problem dictate that only O(1) extra memory can be used

**Pass 1** - In the first pass we find any elements that appear more than twice. The problem already states that the list is sorted.
Therefore, we can keep a variable called `previousValue` and a corresponding variable called `previousCounter` that is used to count
the number of occurences of the value. If this exceeds 2, then we overwrite the value at the index in the array with a "None". This
should remove all additional occurences for values who have > 2 instances.

**Pass 2** - In the second pass, we need to shift the elements, so that the "deleted ones" (i.e. set to None) are pushed to the back
of the list. We iterate through the list, and at each element we overwrite it with `num[i-offset] = num[i]`. This offset starts at zero,
and if we meet a "deleted element" (i.e. None), we increment the offset, and do not perform this write operation. This should shift the
elements that are perfectly fine to the beginning of the list, by overwritting the deleted indexes.

NOTE: The question doesn't require the back of the list to be cleaned up, so we do not need to perform this operation. However, we can
do this easily by using the offset. The offset is the number of deleted values, so we can zero out the last `offset` indicies in the list
to clean it up

## Solution 2 

This uses the approach listed in solution 1, but combines them together into a single pass