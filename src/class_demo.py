class Dict:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.item_count = 0
​
    def get_load_factor(self):
        return self.item_count / self.capacity
​
    def hash_func(self, key):
        bytes_str = key.encode()
        num = 0
        for byte in bytes_str:
            num += byte
        return num % self.capacity
​
    def insert(self, key, value):
        # hash the key            
        index = self.hash_func(key)
        # check if the storage slot, has an item already in there
        if self.storage[index] is not None:
            # First, check if key has already been added
            for item in self.storage[index]:
                # We found a duplicate key, update the value instead
                if item[0] == key:
                    item[1] = value
                    return
            # append the new item to the array
            self.storage[index].append([key, value])
            self.item_count += 1
        # Create an empty array, and add the first item to it
        else:  
            self.storage[index] = [[key, value]]
            self.item_count += 1
        # Check our load factor, and see if we need to resize
        if self.get_load_factor() > 0.7:
            print("We should resize")
            self.resize(self.capacity * 2)
​
    def get(self, key):
        # has the key to get the index
        index = self.hash_func(key)
        if self.storage[index] is None:
            print(f"{key} not found")
            return None
        # search through inner array at the target slot
        for item in self.storage[index]:
            if key == item[0]:
                return item[1]
​
    def delete(self, key):
        # has the key to get the index
        index = self.hash_func(key) 
        self.storage[index] = None
​
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
    def resize(self, new_capacity):
        old_storage = self.storage.copy()    
        # Reset our storage to new capacity
        self.storage = [None] * new_capacity
        self.capacity = new_capacity
        self.item_count = 0
        for slot in old_storage:
            if slot is None:
                continue
            for item in slot:
                self.insert(item[0], item[1])
        
​
​
d = Dict(8)
​
d['apple'] = 'is a fruit'
d['banana'] = 'is also fruit'
d['cucumber'] = 'is a vegetable'
d['peach'] = 'This is definitely not a banana'
print(d.storage)
d['banana'] = 'This is a new value for banana'
d['pineapple'] = 'is a bunch of berries'
# Resize
d['pickle'] = 'is really a cucumber'
print(d.storage)
​
print(d['apple'])
print(d['banana'])
print(d['peach'])
print(d['pickle'])