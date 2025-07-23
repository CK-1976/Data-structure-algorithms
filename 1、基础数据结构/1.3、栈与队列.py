# 栈的多种实现
class ArrayStack:
    """
    基于动态数组的栈实现
    所有操作时间复杂度：O(1)
    """
    def __init__(self):
        self.items = []
        
    def push(self, item):
        """入栈"""
        self.items.append(item)
        
    def pop(self):
        """出栈"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
 
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        
    def is_empty(self):
        """判断栈是否为空"""
        return len(self.items) == 0    
    
    def size(self):
        """返回栈的大小"""
        return len(self.items)    

class LinkStack:
    """
    基于链表的栈实现
    所有操作时间复杂度：O(1)
    """
    class Node:
        def __init__(self, val, next = None):
            self.val = val
            self.next = next
            
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        """入栈 - 在链表头部插入"""
        self.top = self.Node(item, self.top)
        self._size += 1
        
    def pop(self):
        """出栈 - 删除链表头部节点"""
        if self.is_empty():
            raise IndexError(" pop from empty stack")
    
        item = self.top.val
        self.top = self.top.next
        self._size -= 1
        return item
    
    def peek(self):
        """查看栈顶元素"""
        if self.is_empty():
            raise IndexError(" peek from empty stack")
        return self.top.val
    
    def is_empty(self):
        """判断栈是否为空"""
        return self.top is None    
    
    def size(self):
        """返回栈大小"""
        return self._size
    
class MinStack:
    """
    支持O(1)时间获取最小值的栈
    思路：使用辅助栈存储每个状态的最小值
    """
    def __init__(self):
        self.stack =[]      # 主栈    
        self.min_stack = [] # 辅助栈，存储最小值 
        
    def push(self, val):
        """入栈"""
        self.stack.append(val)
        
        # 更新最小值栈
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
            
    def pop(self):
        """出栈"""
        if not self.stack:
            raise IndexError(" pop from empty stack")
        
        self.min_stack.pop()
        return self.stack.pop()
    
    def peek(self):
        """获取栈顶元素"""
        if not self.stack:
            raise IndexError(" peek from empty stack")
        
    def get_min(self):
        """
        获取栈中的最小值
        时间复杂度：O(1)
        """
        if not self.min_stack:
            raise IndexError(" stack is empty")
        return self.min_stack[-1]    
    
# 队列的多种实现
class ArrayQueue:
    """
    基于循环数组的队列实现
    避免了普通数组实现中的元素移动
    """
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0 # 队首指针
        self.rear = 0  # 队尾指针
        self.size = 0
        
    def enqueue(self, item):
        """
        入队
        时间复杂度：O(1)
        """
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        
    def dequeue(self):
        """
        出队
        时间复杂度：O(1)
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        
        item = self.items[self.front]
        self.items[self.front] = None # 避免内存泄漏
        self.front = (self.front + 1) % self.capacity
        self.size  -= 1
        
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        
        return item
    
    def peek(self):
        """查看队首元素"""
        if self.is_empty():
            raise IndexError(" peek from empty queue")
        return self.items[self.front]
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    def _resize(self, new_capacity):
        """调整队列容量"""
        new_items = [None] * new_capacity
        
        # 复制元素到新数组
        for i in range(self.size):
            new_items[i] = self.items[(self.front + i) % self.capacity]
        
        self.items = new_items
        self.capacity = new_capacity
        self.front = 0
        self.rear = self.size
        
# 单调栈与单调队列
