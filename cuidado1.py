
def wrong_user_display(user_metadata = {"name": "John", "age":30}):
    """
    Por su seguridad nunca haga algo parecido a esto. 
    """
    print(user_metadata,"antes del pop")
    name = user_metadata.get("name1",None)
    print(name)
    age = user_metadata.get("age")
    print(user_metadata,"despues del pop")
    return f"{name} ({age})"


def user_display(user_metadata = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}
    print(user_metadata,"antes del pop")
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    print(user_metadata,"despues del pop")
    return f"{name} ({age})"

if __name__=="__main__": 
    wrong_user_display()
    #wrong_user_display({"name": "Jane", "age": 25})
    #wrong_user_display()
    #print("-"*20)
    #user_display()
    #user_display({"name": "Jane", "age": 25})
    #user_display()