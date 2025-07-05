# username = "chaiaurcode"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()

x = 99
# def func2(y):
#     z = x + y
#     return z

# print(func2(1))

# def func3():
#     global x
#     # x = 12 //dont overwrite this again when we delcare global
    
    
# func3()
# print(x)

# def f1():
#     x =88
#     def f2():
#         print(x)
#     return f2()
# myResult = f1()


def chai(num):
    def actual(x):
        return x ** num
    return actual

f = chai(2)

print(f(3))
    
