class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.curr = 0
        if len(list(kwargs.keys())) == 0 or list(kwargs.values()) == [False]: 
            self.ign = False #a != A
            self.set_arr = list(set(self.items))
        elif list(kwargs.values()) == [True]: 
            self.ign = True #a == AÛ
            self.set_arr = []
            for i in self.items:
                if (type(i) is str) and (i.upper() not in self.set_arr and i.lower() not in self.set_arr):
                    self.set_arr.append(i)
                elif i not in self.set_arr and (type(i) is not str): self.set_arr.append(i)
            
    def __next__(self):
        if self.curr < len(self.set_arr):
            res = self.set_arr[self.curr]
            self.curr += 1
            return res
        raise StopIteration 
    
    def __iter__(self):
        return self
    
if __name__ == '__main__':    
    arr = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    #arr = [1,2,2,3,3,1]
    it = Unique(arr, ignore_case = True)
    for el in it:
        print(el)