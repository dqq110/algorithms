#链表
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

#实例化
A = ListNode('a')
B = ListNode('b')
C = ListNode('c')
A.next = B
B.next = C

#遍历链表
tmp = A
while tmp !=None:
    print(tmp.val)
    tmp = tmp.next

#递归遍历链表
def listorder(head):
    if head:
        print(head.val)
        listorder(head.next)
listorder(A)

#翻转一条单向链表:Input: 1->2->3->4->5->NULL
            # Output: 5->4->3->2->1->NULL
#代码实现；
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseList(self,head):
        dummy = head
        tmp = dummy
        while head and head.next != None:
            dummy = head.next
            head.next = dummy.next
            dummy.next = tmp
            tmp = dummy
        return dummy
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
reverse_head = solution.reverseList(head)
tmp = reverse_head
while tmp:
    print(tmp.val)
    tmp = tmp.next