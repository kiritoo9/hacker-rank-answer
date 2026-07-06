class MyQueue(object):

    def __init__(self):
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        return None
        

    def pop(self):
        """
        :rtype: int
        """
        return self.data.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.data[0] if len(self.data) > 0 else None
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.data) <= 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()