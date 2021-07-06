from collections import UserList

class BadList(list):
    
    def __getitem__(self, index):
        
        value = super().__getitem__(index)
        prefix = "even" if index % 2 == 0 else "odd"

        return f"[{prefix}] {value}"
    

class GoodList(UserList):
    
    def __getitem__(self, index):
        
        value = super().__getitem__(index)
        prefix = "even" if index % 2 == 0 else "odd"

        return f"[{prefix}] {value}"
    
if __name__ == '__main__':
    #bl = BadList((0, 1, 2, 3, 4, 5))
    #print(bl[0])
    #print(bl[1])
    #print("".join(bl))
    gl = GoodList((0, 1, 2))
    print(gl[0])
    print(gl[1])
    print("".join(gl))