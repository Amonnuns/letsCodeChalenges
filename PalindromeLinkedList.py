def isPalindrome(self, head) -> bool:
        ls = []
        
        while head != None:
            ls.append(head.val)
            head = head.next
        
        if ls ==ls[::-1]:
            return True
        else:
            return False
    
        
        