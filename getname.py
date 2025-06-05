def getName(name, default="Student"):
    name = input("Enter your name: ")
    if not name:
        return default
    
    return name
print("Hello",getName("name"))
