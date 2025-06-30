class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        result = []

        n = l1
        n_low = l2
        if(self.count(n_low) > self.count(n)):
            n = l2
            n_low = l1

        i = 0
        carry = 0
        len_n = self.count(n)
        len_n_low = self.count(n_low)
        while(i < len_n):

            if(i >= len_n_low):
                t = n.val + carry
                n = n.next
            else :
                t = n.val + n_low.val + carry 
                n = n.next
                n_low = n_low.next

            if(int(t/10)):
                t -= 10
                carry = 1
            else:
                carry = 0
            
            result.append(t)
            i += 1

        if(carry):
            result.append(carry)

        return self.listToLinkedList(result)

    def count(self,list):
        num = 1
        while(list.next):
            list = list.next
            num += 1
        return num
    
    def listToLinkedList(self,nums):
        dummy = ListNode(0)

        current = dummy
        for num in nums:
            current.next = ListNode(num)
            current = current.next

        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

s = Solution()

n3 = ListNode(3)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)


p3 = ListNode(4)
p2 = ListNode(6, p3)
p1 = ListNode(5, p2)

print(s.addTwoNumbers(n1 ,p1))