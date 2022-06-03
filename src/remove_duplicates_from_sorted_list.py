class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        lastUniqueNode = head
        currentNode = head.next
        while currentNode is not None:
            ## When we switch node values
            if currentNode.val != lastUniqueNode.val:
                lastUniqueNode.next = currentNode                    
                lastUniqueNode = currentNode
                
            currentNode = currentNode.next
            
        ## For the end of the LinkedList
        lastUniqueNode.next = None                    
        return head
        
