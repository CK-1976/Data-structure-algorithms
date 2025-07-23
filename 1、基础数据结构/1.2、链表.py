# 单链表实现
class ListNode:
    """链表节点"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    """
    单链表实现
    支持头部/尾部插入删除、反转、环检测等操作
    """
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_first(self, val):
        """
        在链表头部添加节点
        时间复杂度：O(1)
        """
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def add_last(self, val):
        """
        在链表尾部添加节点
        时间复杂度：O(n)
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            # 遍历到最后一个节点
            current = self.head
            while current.next:
                current = current.next
                
            current.next = new_node
            
        self.size += 1
        
    def add_at_index(self, index, val):
        """
        在指定位置插入节点
        时间复杂度：O(n)
        """
        if index < 0 or index >self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.add_first(val)
            return
        
        # 找到插入位置前的前面一个节点
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1
        
    def remove_first(self):
        """
        删除头节点
        时间复杂度O(1)
        """
        if not self.head:
            raise IndexError("Remove from empty list")
        
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
        
    def remove_last(self):
        """
        删除尾节点
        时间复杂度：O(1)
        """
        if not self.head:
            raise IndexError("remove from empty list")
        
        if not self.head.next:
            return self.remove_first()
        
        # 找到倒数第二个节点
        current = self.head
        while current.next.next:
            current = current.next
            
        val = current.next.val
        current.next = None
        self.size -= 1
        return val
    
    def reverse(self):
        """
        反转链表 - 迭代法
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        prev = None
        current = self.head
        
        while current:
            # 保存下一个节点
            next_temp = current.next
            # 反转指针
            current.next = prev
            # 移动指针
            prev = current
            current = next_temp
        
        self.head = prev    
    
    def reverse_recurisve(self):
        """
        反转链表 - 递归法
        时间复杂度：O(n)
        空间复杂度：O(n) 递归调用栈
        """
        def reverse_helper(node):
            # 基础情况：空链表或只有一个节点
            if not node or not node.next:
                return node

            # 递归反转后续链表
            new_head = reverse_helper(node.next)
            
            # 反转当前与下一个节点的指向
            node.next.next = node 
            node.next = None
            
            return new_head
        
        self.head = reverse_helper(self.head)
        
    def find_middle(self):
        """
        找到链表中点 - 快慢指针法
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not self.head:
            return None
        
        slow = fast = self.head
        
        # 快指针每次走两步，慢指针每次走一步
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow     
    
    def has_cycle(self):
        """
        检测链表是否有环 - Floyd判圈算法
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not self.head:
            return False
        
        slow = fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # 快慢指针相遇
            if slow == fast:
                return True
        
        return False
    
    def find_cycle_start(self):
        """
        找到环的起始节点
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if not self.head:
            return False
        
        slow = fast = self.head
        
        # 第一步：判断是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None # 无环
        
        # 第二步：找到环的起点
        # 将slow重置到头部，两个指针同速前进
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow
    
    def merge_sorted(self, other):
        """
        合并两个有序链表
        时间复杂度：O(m + n)
        空间复杂度：O(1)
        """
        dummy = ListNode(0) # 哨兵节点
        tail = dummy
        
        p1,p2 = self.head,other.head
        
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
        
        # 连接剩余节点
        tail.next = p1 if p1 else p2
        
        self.head = dummy.next
        
        self.size += other.size
                
# 双向链表的实现
class DoublyListNode:
    """双向链表节点"""
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkList:
    """
    双向链表实现
    相比单链表,可以O(1)时间删除给定节点
    """        
    def __init__(self):
        # 使用哨兵节点简化边界处理
        self.head = DoublyListNode # 头哨兵
        self.tail = DoublyListNode # 尾哨兵
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0    
     
    def add_frist(self, val):
        """在头部添加节点"""
        self._add_between(val, self.head, self.head.next)
    
    def add_last(self, val):
        """在尾部添加节点"""
        self._add_between(val, self.tail.prev, self.tail)
    
    def _add_between(self, val, pred, succ):
        """在pred和succ之间插入新节点"""
        new_node = DoublyListNode(val, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node    
    
    def remove_node(self, node):
        """
        删除给定节点
        时间复杂度O(1)
        """     
        if node == self.head or node == self.tail:
            raise ValueError("Can not remove sentinel nodes")
        
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        return node.val
    
    def remove_first(self):
        """删除第一个节点"""
        if self.size == 0:
            raise IndexError("Remove from empty list")
        
        return self.remove_node(self.head.next)
    
    def remove_last(self):
        """删除最后一个节点"""
        if self.size == 0:
            raise IndexError("Remove from emoty list")
        
        return self.remove_node(self.tail.prev)
    
    def __str__(self):
        """字符串表示"""
        values = []
        current = self.head.next
        while current != self.tail:
            values.append(str(current.val))
            current = current.next
        return '<->'.join(values)