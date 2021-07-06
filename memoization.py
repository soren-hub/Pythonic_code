import os as os
#import

#Decorator for time measurement  
def measure_time(function):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print('Time:' ,total, 'seconds' )
        return result

    return wrapper

#Memorization implementation using class
class Memorization:
    def __init__(self, func):
        self.func = func
        #history dictionary to store past results
        self.history = {}
        self._memory = os.size(self.history)
        
    #__call__ to implement Memoization    
    def __call__(self, *args):
        if args not in self.history:
            self.history[args] = self.func(*args)
        return self.history[args]

def fibonacci(n):
    return fibonacci(n-1) + fibonacci(n-2) if n > 1 else n
         
@Memorization
def fibonacci_acelerated(n):
    return fibonacci_acelerated(n-1) + fibonacci_acelerated(n-2) if n >1 else n


@measure_time 
def time_fibonacci(n,acelerated=False): 
    print("-"*20)
    print("{}th fibonacci number".format(n))
    return fibonacci_acelerated(n) if acelerated  else fibonacci(n)


if __name__ == '__main__':
    #print(time_fibonacci(30),"normal implementation")
    print(time_fibonacci(100,acelerated=True),"acelerated implementation")
    
    
 