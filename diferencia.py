class WithoutCall: 
    
    def __init__(self): 
        print("__init__ : WithoutCall")


class WithCall: 
    
    def __init__(self): 
        print("__init__: WithCall")

    def __call__(self): 
        print("__call__ : call")
        
        
if __name__=="__main__":
    sin_call = WithoutCall()
    con_call = WithCall()
    con_call()    