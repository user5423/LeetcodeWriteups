
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## We create a sentinel node to more easily
        sentinelNode = ListNode(None, head)

        ## If we have less than two items, we return the head
        if sentinelNode.next == None or sentinelNode.next.next == None:
            return sentinelNode.next
        
        ## otherwise we have 2 items or more
        first = sentinelNode
        second = first.next
        third = second.next
        
        counter = 3
        while third != None:
            ## Our counter uses % 3 instead of % 2, since `% 3 == 0` means execute every 2 steps, 
            ## where as `% 2 == 0` results in execution every other stepstep
            if counter % 3 == 0:
                ## perform swap
                first.next = third
                second.next = third.next
                third.next = second
                
            counter += 1
            ## push variable references up by one node
            first = second
            second = third
            third = third.next
            
        return sentinelNode.next
                
            
        
        