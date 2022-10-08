# 사전초기화 방법
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
a = Singleton()
b = Singleton()
print(a.instance)
print(b.instance) 
print(a == b)
# 늦은초기화 방법
class Singleton:
    _instance = None
    def __init__(self):
        if not Singleton._instance:
            print("__init__ method called but nothing is created")
        else:
            print("instance already created:", self.get_instance())
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance

a = Singleton()
a.get_instance()
b = Singleton()




# class Point():
#     def __new__(cls,*args,**kwargs):
#         print("From new")
#         print(cls)
#         print(args)
#         print(kwargs)
#         # create our object and return it
#         objs = super().__new__(cls)
#         return objs
    
#     def __init__(self, x = 0, y = 0):
#         print("From init")
#         self.x = x
#         self.y = y

#     def add(self):
#         return self.x + self.y

#     def is_there(cls):
#         if not hasattr(cls, "add"):
#             print("no")
#         else:
#             print("yes")
# a = Point(3,4)

# c = a.add()
# print(c)
# a.is_there()



# class Math:
#     @staticmethod
#     def factorial(number):
#         if number == 0:
#             return 1
#         else:
#             return number * Math.factorial(number - 1)
       
# factorial = Math.factorial(5)
# print(factorial)


# class Test:
#     def __init__(self):
#         print("init 호출")
    
#     def __call__(self):
#         print("call 호출")

#     def test(self):
#         print("test호출")    

# a = Test()

# a.test()