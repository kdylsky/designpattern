"""
심플팩토리
"""
from abc import ABCMeta, abstractmethod
# 추상클래스이다.
# Job을 상속받는 모든 클래스는 아래의 do_something를 반드시 오버라이딩해주어야한다.
# 추상클래스를 이용함으로써 오버라이딩에 대해서 강제하고 있다.

class Job(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass

class Student(Job):
    # 상속받은 추상클래스의 메서드를 오버라이딩한다.
    def do_something(self):
        print("Let's do the study")
    
class Worker(Job):
    # 상속받은 추상클래스의 메서드를 오버라이딩한다.
    def do_something(self):
        print("Lets' do the work")

# 팩토리에 해당한다.
# 다른 클래스의 객체를 생성한다.
class SimpleFactory(object):
    # 다른클래스의 객체와 관련된 메서드와 그 인자를 포함해서 객체를 생성한다.
    def do_it(self, object_type):
        return(eval(object_type.capitalize())().do_something())

# job = input("what is your job? Student? Worker?")
# 팩토리로 팩토리안에 들어있는 객체를 생성한다.
# 인자로 student/worker를 받아서 해당하는 클래스의 객체를 생성하게 된다.
# f = SimpleFactory()
# f.do_it(job)



