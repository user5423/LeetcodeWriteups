# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinelNode = ListNode(val=None, next=head)
        isDuplicate = False
        
        lastSwitchNode = sentinelNode
        previousNode = sentinelNode
        currentNode = sentinelNode.next
        while currentNode != None:
            if currentNode.val == previousNode.val:
                isDuplicate = True
            else:
                if isDuplicate:
                    lastSwitchNode.next = currentNode
                    isDuplicate = False
                    ## Below is performed for a cleanup (Not needed in the question)
                    # previousNode.next = None
                else:
                    lastSwitchNode = previousNode
                    
            previousNode = currentNode
            currentNode = currentNode.next
        
        if isDuplicate:
            lastSwitchNode.next = currentNode
            isDuplicate = False
            ## Below is performed for a cleanup (Not needed in the question)
            # previousNode.next = None
            
        return sentinelNode.next
        