# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinelNode = ListNode(next, head)

        if head.next == None:
            return head
        
        previousNode = sentinelNode
        currentNode = sentinelNode.next ## head

            previousNode = currentNode
            currentNode = currentNode.next
        
        leftNode = currentNode
        beforeLeftNode = previousNode
        
        for counter in range(left, right+1):
            oldCurrentNode = currentNode
            newCurrentNode = currentNode.next
            
            oldCurrentNode.next = previousNode
            
            ## Fix up for next iteration
            currentNode = newCurrentNode
            previousNode = oldCurrentNode
            
            
        rightNode = oldCurrentNode
        afterRightNode = newCurrentNode
        
        ## Flip right to left
        beforeLeftNode.next = rightNode
        leftNode.next = afterRightNode
        
        ## Return head of linked list
        return sentinelNode.next
        

        ## Case Analysis
        
        
        ## Case 0: Single LinkedList
        ## return head
             
        ## Case 1: Multiple LinkedList
        ## 1. We iterate until we get to the left node
        ## -- we store a ref to left
        ## -- we store a reft to before-left
        ## 2. We then continue iterating until the right node
        ## -- for each iteration we switch the direction of the pointer
        ##  Once we hit the right node,
        ## -- we store a ref to right
        ## -- we store a ref to after-right
        ## 3. We then flip right and left
        ## -- beforeLeft.next = right
        ## -- left.next = afterRight
        ## 4. return sentinel.next
        
        ## Case 1a: left.next == right        
        ## let left = 5
        ## let beforeLeft = 4
        ## let right = 6
        ## left afterRight = 7
        ## NOTE: This is fine as long as we start iterating from left on the second for loop instead of left.next
        
        ## Case 1b: left == head
        ## This is fine since we have the sentinel Node
        
        ## Case 1c: right.next == None
        ## THis should be fine aswell

