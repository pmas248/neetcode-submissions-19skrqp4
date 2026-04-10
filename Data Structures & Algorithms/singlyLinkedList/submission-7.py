class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        else:
            curr = self.head.next
            for i in range(index):
                curr = curr.next
            return curr.val

    def insertHead(self, val: int) -> None:
        newnode = ListNode(val)
        newnode.next = self.head.next
        self.head.next = newnode

        if self.size == 0: #if no previous nodes
            self.tail = newnode

        self.size += 1

    def insertTail(self, val: int) -> None:
        newnode = ListNode(val)
        self.tail.next = newnode
        self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        prev = self.head
        for i in range(index):
            prev = prev.next

        if prev.next == self.tail:
            self.tail = prev

        prev.next = prev.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
