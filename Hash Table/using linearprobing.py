class HashTable:
    def __init__(self,size):
        self.size=size
        self.hash_table=[None]*size
    
    def hash_function(self,key):
        return hash(key)%self.size
    
    def add(self,key,value):
        index=self.hash_function(key)
        while self.hash_table[index] is not None:
            index=(index+1)% self.size
        self.hash_table[index]=(key,value)

    def delete(self, key):
        index = self.hash_function(key)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                self.hash_table[index]=None
            index = (index + 1) % self.size
        return None
    
    def get(self,key):
        index=self.hash_function(key)
        while self.hash_table[index] is not None:
            if self.hash_table[index][0]==key:
                return self.hash_table[1]
            index=(index+1)%self.size
        return None
    

h=HashTable(10)
h.add(1,'abhi')
h.add(3,'jawhar')
h.add(3,'shamal')
h.add(6,'thomas')
print(h.hash_table)


h.delete(6)

print(h.hash_table)




