
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ## Create two linked lists via sentinel nodes
        ## iterate through the list and add it the newest node in either one of the ll
        
        ## Case Analysis
        ## Case 0 - Empty list
        ## -- return head
        ## Case 1 - Single item list
        ## -- return head
        ## Case 2 - Multiple item list
        ## -- we nee further processing
        
        sentinelNode = ListNode(None, head)
        
        ## This handles case-0 and case-1
        if sentinelNode.next == None or head.next == None:
            return head
        
        ## We need to handle case-2
        ## we create two sentinel nodes
        leftSentinel = ListNode(None, None)
        left = leftSentinel
        
        rightSentinel = ListNode(None, None)
        right = rightSentinel
        
        ## Iterate through the original ll
        currentNode = sentinelNode.next
        while currentNode != None:
            if currentNode.val < x:
                left.next = currentNode
                left = currentNode
            else:
                right.next = currentNode
                right = currentNode
                
            currentNode = currentNode.next
                
        ## We now need to merge the two linkedlists together
        
        ## NOTE: They both cannot be empty, (only one can be max)
                
        ## Case Analysis
        ## Case 1: left is empty
        ## -- return right
        ## Case 2: right is empty
        ## -- return left
        ## Case 3: neither are empty
        ## -- merge them together
            
        left.next = None
        right.next = None
        
        if leftSentinel.next is None:
            return rightSentinel.next
        elif rightSentinel.next is None:
            return leftSentinel.next
        else:
            left.next = rightSentinel.next
            return leftSentinel.next
            

        