class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## Requirements
        ## - Input
        ## --> head (of a linkedList)
        ## --> k (number of places to rotate by)
        ## - Output
        ## --> head of rotated list
        
        ## Case Analysis
        
        ## Case 0 - empty list
        ## -- return head
        ## Case 1 - single item list
        ## -- return head
        ## Case 2 - multiple item list
        ## -- perform rotation
        
        sentinelNode = ListNode(None, head)
        
        ## If case-0 or case-1, we return the head
        if sentinelNode.next == None or sentinelNode.next.next == None:
            return sentinelNode.next
        
        ## otherwise, we are in case-2
        ## - we make the linkedList into a circular linked list
        ## - we find the node that is k^th from the end of the linkedlist
        ## - we then bind this to a variable called `newHead`
        ## - and we cleanup the references so that no node has a .next reference
        ## that points to this new head node.
        ## NOTE: This inclusively works for nodes at index 0 or -1 of the list
        
        currentNode = sentinelNode
        counter = 0
        while currentNode.next != None:
            counter += 1
            currentNode = currentNode.next
            
        length = counter
        k = k % length
        currentNode.next = head
        
        previousNode = sentinelNode
        currentNode = previousNode.next
        counter = length
        while counter != k:
            counter -= 1
            previousNode = currentNode
            currentNode = currentNode.next
            
            
        newHead = currentNode
        previousNode.next = None
        
        return newHead
        
            
        
 