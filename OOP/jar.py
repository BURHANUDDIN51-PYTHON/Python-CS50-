class Jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self._size = 0
        
    def __str__(self):
        return self.size * "🍪"
    
    
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size
    
    @capacity.setter
    def capacity(self, capacity):
        if int(capacity):
            self._capacity = capacity
        else:
            raise ValueError
        
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n 
       
        
    def withdraw(self, n):
        if self.size < self.capacity and self.size > 0:
            if self.size - n > 0:
                self._size -= n 
                 
        else: 
            raise ValueError
        
        
    
    
jar = Jar(12)
jar.deposit(10)
jar.withdraw(5)
print(jar)