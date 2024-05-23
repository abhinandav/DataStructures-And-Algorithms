class HashTable:
    def __init__(self,size):
        self.size=size
        self.hash_table=[None]*size
    
    def hash_function(self,key):
        return hash(key)%self.size
    
    def add(self,key,value):
        index=self.hash_function(key)
        if self.hash_table[index] is None:
            self.hash_table[index]=[(key,value)]
        else:
            self.hash_table[index].append((key,value))

    def delete(self,key):
        index=self.hash_function(key)
        if self.hash_table[index] is not None:
            for i,pair in enumerate(self.hash_table[index]):
                if pair[0]==key:
                    self.hash_table[index]=None
        return None
    
    def get(self,key):
        index=self.hash_function(key)
        if self.hash_table[index]is not None:
            for pair in self.hash_table[index]:
                if pair[0]==key:
                    return pair[1]
        return None
    

h=HashTable(10)
h.add(1,'abhi')
h.add(3,'jawhar')
h.add(3,'shamal')
h.add(6,'thomas')
print(h.hash_table)


h.delete(6)

print(h.hash_table)




