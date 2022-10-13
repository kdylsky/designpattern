"""
전략패턴
"""
from abc import abstractmethod, ABC

class Scheduler(ABC):
    @abstractmethod
    def get_next_call(self):
        pass
        
        # 정책 패턴을 사용하지 않으면 메서드 마다 if-else구문으로 들어갈것이다.
        # if RoundRobin
        # elif LeastJob
        # elif priorityAllocation
        # 이후에 정책이 추가되면 계속 해서 if-else구문으로 추가될 것이다.
    
    @abstractmethod
    def senf_call_to_agent(self):
        pass

        # 정책 패턴을 사용하지 않으면 메서드 마다 if-else구문으로 들어갈것이다.
        # if RoundRobin
        # elif LeastJob
        # elif priorityAllocation
        # 이후에 정책이 추가되면 계속 해서 if-else구문으로 추가될 것이다.
    

class RoundRobin(Scheduler):
    def get_next_call(self):
        print("상담 전화를 순서대로 대기열에서 가져옵니다.")


    def senf_call_to_agent(self):
        print("다음 순서 상담원에게 배분합니다.")

class LeastJob(Scheduler):
    def get_next_call(self):
        print("상담 전화를 순서대로 대기열에서 가져옵니다.")


    def senf_call_to_agent(self):
        print("현재 상담업무가 없거나 상담개기가 가장 작은 삼당원에게 할당합니다.")


class PriorityAllocation(Scheduler):
    def get_next_call(self):
        print("고객 등급이 높은 고객의 전화를 먼저 가져옵니다.")


    def senf_call_to_agent(self):
        print("업무 능력이 좋은 상담원에게 우선 배분한다.")

# 이후에 정책이 추가되면, 클래스레벨에서 추가로 구현하면 된다.
# 기존에 있는 클래스에 영향을 주지 않는다.

class SchdulerContext:
    def __init__(self):
        self.__schdulertest_strategy = None

    def get_next_call(self):
        self.__schdulertest_strategy.get_next_call()
    
    def senf_call_to_agent(self):
        self.__schdulertest_strategy.senf_call_to_agent()
    
    @property
    def schdulertest_strategy(self):
        return self.__schdulertest_strategy
    
    @schdulertest_strategy.setter
    def schdulertest_strategy(self, strategy):
        self.__schdulertest_strategy = strategy


class A_company(SchdulerContext):
    def __init__(self):
        super().__init__()
        print("a컴퍼니 입니다.")

class B_company(SchdulerContext):
    def __init__(self):
        super().__init__()
        print("b컴퍼니 입니다.") 

a = A_company()
a.schdulertest_strategy = RoundRobin()
a.get_next_call()
a.senf_call_to_agent()

b = B_company()
b.schdulertest_strategy = PriorityAllocation()
b.get_next_call()
b.senf_call_to_agent()

a.schdulertest_strategy = LeastJob()
a.get_next_call()
a.senf_call_to_agent()


# ch = input()
# schdulertest = None

# if ch == "R" or ch == "r":
#     schdulertest = RoundRobin()
# elif ch == "L" or ch == "l":
#     schdulertest = LeastJob()
# elif ch == "P" or ch == "p":
#     schdulertest = PriorityAllocation()
# else:
#     print("no support")

# schdulertest.get_next_call()
# schdulertest.senf_call_to_agent()

# 기능에 세트가 있는데, 세트가 다양한 방법으로 구현될 수 있는 경우 if-else구문을 사용하지 않고 클래스로 분류하고,




"""
전략패턴을 사용하지 않은 경우
"""
class NotStrategy:
    def __init__(self):
        pass
    @abstractmethod
    def cry(self):
        pass

class Dog(NotStrategy):
    def __init__(self):
        print("나는 개")
    def cry(self):
        print("왈왈")    

class Person(NotStrategy):
    def __init__(self):
        print("나는 사람")
    def cry(self):
        print("울지 않아")
 
person = Person()
dog = Dog()

person.cry()
dog.cry()


"""
전략패턴
"""
class SoundStrategy(ABC):
    @abstractmethod
    def cry(self):
        pass

class CryStrategy(SoundStrategy):
    def cry(self):
        print("왈왈")
    
class NotCryStrategy(SoundStrategy):
    def cry(self):
        print("울지 않아")

class CryingContext:
    def __init__(self):
        self.__sound_strategy = None

    def cry(self):
        self.__sound_strategy.cry()
    
    @property
    def sound_strategy(self):
        return self.__sound_strategy

    @sound_strategy.setter
    def sound_strategy(self, strategy):
        self.__sound_strategy = strategy

class Dog(CryingContext):
    def __init__(self):
        super().__init__()
        print("나는 개")

class Person(CryingContext):
    def __init__(self):
        super().__init__()
        print("나는 사람")

person = Person()
dog = Dog()

person.sound_strategy = NotCryStrategy()
dog.sound_strategy = CryStrategy()

person.cry()
dog.cry()

person.sound_strategy = CryStrategy()
person.cry()





"""
전략패턴
"""

class PayMethodStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

class ACardStrategy(PayMethodStrategy):
    def __init__(self, name, cardNumber, ccv, date):
        self.name = name
        self.cardNumber = cardNumber
        self.ccv = ccv
        self.date = date
        self.is_visa = False
    def pay(self, amount):
        print("use ACard")

class BCardStrategy(PayMethodStrategy):
    def __init__(self, name, cardNumber, ccv, date):
        self.name = name
        self.cardNumber = cardNumber
        self.ccv = ccv
        self.date = date
        self.is_visa = True
    def pay(self, amount):
        print("use BCard")

class Item:
    def __init__(self, name, cost, is_visa):
        self.name = name
        self.cost = cost
        self.is_visa = is_visa

    def pay(self, paymethod):
        if self.is_visa == True :
            if paymethod.is_visa== True:
                paymethod.pay(self.cost)
            else:
                print("다른 카드로 결제하세요")
        else:
            paymethod.pay(self.cost)
            print("결제가 완료 되었습니다.")

acard = ACardStrategy("ehdus", 1000, 1000, 1000)
bcard = BCardStrategy("ehdus", 2000, 2000, 2000)

banana = Item("바나나", 100, True)

banana.pay(acard)
banana.pay(bcard)