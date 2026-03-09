class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value = value
        self.k = k 
        self.stream = deque()
        

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num != self.value:
            self.stream.clear()
        else:
            self.stream.append(num)
        if self.k < len(self.stream):
             self.stream.popleft()

        if len(self.stream) == self.k:
            return True
        return False


# Your DataStream object will be instantpiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)