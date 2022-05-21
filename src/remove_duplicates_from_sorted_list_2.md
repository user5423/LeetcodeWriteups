# Maximum Length of a Concatenated String with Unique Characters (Medium)

Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# 

## Solution 1

Runtime: **33 ms**, faster than **98.92%** of Python3 online submissions for Remove Duplicates from Sorted List II.
Memory Usage: **13.7 MB**, less than **98.29%** of Python3 online submissions for Remove Duplicates from Sorted List II.

### Implementation

We start by creating a sentinel node, which enables use to deal with edge cases such as empty linked lists
The main concept of the approach is that we have a checkpoint system. We iterate through the list, and since
it is sorted, we can be sure of whether a node is a duplicate, once we have moved to a node with a new value.
(e.g. we know that 2 is distinct, where `None -> 1 -> 2 -> 4`, by the time we have reached 4). This is done
by keeping a variable of the previous element - i.e. since they are sorted, duplicates must be contiguous.

If we move to a node of a new value, and no duplicates haven't been found at this point, then we know that
the part of the linked list we have scanned through is safe. Therefore, we update our checkpoint to the previous
node. In the example `None -> 1 -> 2 -> 4`, once we move from `1 -> 2`, we know that `1` has no duplicates, so 
we set it as our checkpoint once we reach `2`. We do the same thing form `2->4` - we know that `2` has no 
duplicates so we set it as our checkpoint once we reach `4`.

If we find that a duplicated element then we can bypass it. In the example `None -> 1 -> 2 -> 4 -> 4 -> 5`, we
are at the first node with value `4`. We keep iterating through, and we find out at the second node with `4` that
it is a duplicate since the previous value was `4`. Therefore we keep on iterating until we have reached a node
with a new value.

Once we reach this node with a new value, we use our checkpoint node (that we know is safe), and set its `.next`
reference to be this new value - this essentially bypasses any duplicate nodes. We also set the last duplicate
(i.e. previousNode) to point to None, instead of the current element - (this isn't neccessary but a nice cleanup)
- we go from `None -> 1 -> 2 -> 4 -> 4 -> 5`
- to `None -> 1 -> 2 -> 5`
We do not update the checkpoint until we know that the current element (i.e. now it is `5`), is not a duplicate

Once we've iterated through the list, we return the `sentinelNode.next` value. If it is an empty list, then `None`
is returned, otherwise, we have returned the head value of the duplicate free list.

**[Python Code Implementation](remove_duplicates_from_sorted_list_2.py2.py)**