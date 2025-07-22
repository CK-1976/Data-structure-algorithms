# 动态数组实现
class DynamicArray:
    """
    动态数组实现，支持自动扩容和缩容
    时间复杂度：
    - 访问 O(1)
    - 插入末尾 O(1) 摊还
    - 插入任意位置 O(n)
    - 删除 O(n)
    """
    def __init__(self,initial_capacity=10):
        self.capacity = initial_capacity # 数组容量
        self.size = 0 # 元素当前个数
        self.data = [None] * self.capacity # 底层数组
        
    def __len__(self):
        """返回数组长度"""
        return self.size
    
    def getitem(self, index):
        """"支持下标访问"""
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of range [0, {self.capatiy})")
        return self.data[index]
    
    def setitem(self, index, value):
        """支持下标赋值"""
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size})")
        self.data[index] = value
        
    def append(self, value):
        """在末尾添加元素"""
        # 如果容量满了，扩容为原来的两倍
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.data[self.size] == value
        self.size += 1
        
    def insert(self, index, value):
        """在指定位置插入元素"""
        if not 0 <= index <= self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size})")
        
        # 容量检查
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        # 将index及之后一位的元素后移一位
        for i in range(self.size, index ,-1):
            self.data[i] = self.data[i+1]
            
        self.data[index-1] = value
        self.size += 1
   
    def remove(self, index):
        """移除指定位置的元素"""
        if not 0 <= index < self.size:
            raise IndexError(f"Index {index} out of rang [0, {self.size})")
        
        removed_value = self.data[index]
        
        # 将index之后的元素前移一位
        for i in range(index, self.size-1):
            self.data[i] = self.data[i+1]
            
        self.size -= 1
        self.data[self.size] = None # 防止内存泄漏
        
        if self.size > 0 and self.size < self.capacity // 4:
            self._resize(self.capacity // 2)
        
        return removed_value
    
    def _resize(self, new_capacity):
        """调整数组容量"""
        new_data = [None] * new_capacity
        # 复制原有数据
        for i in range(self.size):
            new_data[i] = self.data[i]
            
        self.data = new_data
        self.capacity = new_capacity
        
    def __str__(self):
        """字符串表示"""
        return str([self.data[i] for i in range(self.size)])
    
# 字符串算法基础
class StringAlgorithms:
    """字符串基础算法集合"""
    
    @staticmethod
    def reverse_string(s):
        """
        反转字符串 - 多种实现方式
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        # 方法1：切片
        # return s[::-1]
        
        # 方法2：双指针原地反转（如果是字符数组）
        chars = list(s)
        left,right = 0, len(chars) - 1
        while left < right :
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -=1
            
        return ''.join(chars)
    
    @staticmethod
    def is_palindrome(s:str):
        """
        判断是否为回文串
        时间复杂度：O(n)
        空间复杂度：O(1)
        """        
        # 预处理：只保留数字和字母，转化为小写
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        
        # 双指针判断
        left, right = 0, len(s)-1,
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -=1
        return True
    
    @staticmethod
    def longest_common_prefix(strs):
        """
        最长公共前缀
        时间复杂度：O(n*m) n为字符串数量，m为最短字符串长度
        空间复杂度：O(1)
        """
        if not strs:
            return ""
        
        # 纵向扫描法
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or char != str[j][i]:
                    return strs[0][:i]
        
        return strs[0]
    
    @staticmethod
    def group_anagrams(strs):
        """
        字母异位词分组
        时间复杂度：O(n*k*log(k)) n为字符串数量，k为字符串平均长度
        空间复杂度：O(n*k)
        """
        from collections import defaultdict
        
        #  使用排序后的字符串作为key
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 将字符串排序作为key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
            
        return list(anagram_map.values())