class MinStack(object):

    def __init__(self):
        self.values = []
        self.min = []

    def push(self, val):
        self.values.append(val)
        if self.min:
            val =  min(val,self.min[-1])
        self.min.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.values.pop()
        """
        :rtype: None
        """
        

    def top(self):
        """
        :rtype: int
        """
        return self.values[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        

obj = MinStack()
obj.push(2)
obj.push(7)
obj.push(-3)
print(obj.top())
print(obj.values)
print(obj.getMin())
# Your MinStack object will be instantiated and called as such:
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()