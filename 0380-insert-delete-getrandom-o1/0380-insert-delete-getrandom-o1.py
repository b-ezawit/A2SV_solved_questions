class RandomizedSet(object):

    def __init__(self):
        self.values = []
        self.valueIndx = {} 

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.valueIndx:
            self.valueIndx[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.valueIndx:
            index = self.valueIndx[val]
            lastItem = self.values[-1]
            self.values[index], self.values[-1] = self.values[-1] , self.values[index]
            self.valueIndx[lastItem] = index
            del self.valueIndx[val]
            self.values.pop()
            return True
        
        return False
              

    def getRandom(self):
        """
        :rtype: int
        """
        randomIndx = random.randint(0 , len(self.values)-1)
        return self.values[randomIndx]

   

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()