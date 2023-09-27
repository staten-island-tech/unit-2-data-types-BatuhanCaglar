westbound = ("true")
eastbound = ("false")
def traffic():
    if westbound == "false" and eastbound == "true":
        print("true")
    elif westbound == "true" and eastbound == "false":
        print("true")
    if westbound == "false" and eastbound == "false":
        print("true")
    else:  
        print("false")  