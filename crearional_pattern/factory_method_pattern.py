"""
팩토리 메서드
"""

from abc import abstractmethod, ABC

# 추상클래스
class RobatPart(ABC):
    @abstractmethod
    def assemble(self):
        pass

class HeadPart(RobatPart):
    def assemble(self):
        print("assemble head part")

class WingPart(RobatPart):
    def assemble(self):
        print("assemble wing part")

class LegPart(RobatPart):
    def assemble(self):
        print("assemble leg part")

class BodyPart(RobatPart):
    def assemble(self):
        print("assemble body part")

class ArmPart(RobatPart):
    def assemble(self):
        print("assemble arm part")


# 추상클래스
class Robot(ABC):
    def __init__(self):
        self.parts = []
        self.create_robot()

    @abstractmethod
    def create_robot(self):
        pass

    def add_part(self,part):
        self.parts.append(part)
    
    def assemble_part(self):
        for part in self.parts:
            part.assemble()

# 팩토리
# 실제로 객체를 생성한다.
# 객체가 어떻게 생성될 것인지를 결정한다.
class DogRobot(Robot):
    def create_robot(self):
        self.add_part(HeadPart())
        self.add_part(BodyPart())
        self.add_part(ArmPart())
        self.add_part(LegPart())



class BirdRobot(Robot):
    def create_robot(self):
        self.add_part(HeadPart())
        self.add_part(BodyPart())
        self.add_part(WingPart())
        self.add_part(LegPart())


# dog_robot = DogRobot()
# dog_robot.assemble_part()




# 추상클래스로 만든다.
# 필요한 메서드는 하위클래스에서 재정의한다.
class Car(ABC):
    cartype = None
    def __str__(self):
        return self.cartype

class Santafe(Car):
    def __init__(self):
        self.cartype = "santafe"


class Sonata(Car):
    def __init__(self):
        self.cartype = "sonata"

# 팩토리의 상위클래스로 상위클래스에서는 팩토리에서 사용될 공통의 기능을 정의해준다.
class CarFactory(ABC):
    # 팩토리에서 사용될 공통 개념
    @abstractmethod
    def create_car(self, name):
        pass

    def numbering(self):
        print("numbering")

    def washing(self):
        print("washing")    
    
    # create_car메서드에 대한 구현을 하면 된다.
    def sell_car(self, name):
        self.numbering()
        self.create_car(name)
        self.washing()

# 팩토리에 해당한다.
# 들어오는 인자에 따라서 생성되는 객체가 달라진다.  
# 실제 코드 상에서 if-else로 사용하면 코드가 지저분해진다. 팩토리클래스를 사용하면 깔끔해진다.
# 팩토리를 두고 팩토리의 조건에 따라 생성되는 객체가 달라진다.
# 여기서 조건은 들어오는 인자(name)에 해당한다.
class HyundaiCarFactory(CarFactory):
    def create_car(self, name):
        if name == "sonata":
            car = Sonata()
        elif name == "santafe":
            car = Santafe()

        return car

# 인자에 따라서 생성되는 객체가 달라지기 때문에 enum에 넣어서 관리하면 좀더 효율적인 관리가 가능하다. 
factory = HyundaiCarFactory()
new_car = factory.create_car("sonata")
new_car2 = factory.create_car("santafe")









# 상품에 대한 추상클래스로 만든다.
# 필요한 메서드는 하위클래스에서 재정의한다.
class Car(ABC):
    cartype = None
    def __str__(self):
        return self.cartype

class Santafe(Car):
    def __init__(self):
        self.cartype = "santafe"

class Sonata(Car):
    def __init__(self):
        self.cartype = "sonata"


class CarFactory(ABC):
    @abstractmethod
    def returnCar(self, name):
        pass

class HyundaiCarFactory(CarFactory):
    
    carmap = {}
    
    def returnCar(self, name):
        car = self.carmap.get(name)

        if car == None:
            if name == "tomas":
                car = Sonata()
            elif name == "james":
                car = Santafe()
            
            self.carmap[name] = car

        return car
    # 인스턴스를 관리하는 것이다.
    # 없으면 생성하고, 있으면 있는 인스턴스를 반환한다.
    # 키 값에 해당하는 유일한 인스턴스 일 경우 사용가능하다.



factory = HyundaiCarFactory()

# 상황에 따라(어떤 인자가 들어왔냐에 따라서) 다양한 인스턴스를 생성할 수 잇다.
# 어떤 인자가 들어왔냐에 따라서 다양한 인스턴스를 만들 수 있다.
# map에서 관리를 해서 동일한 인스턴스를 반환하기도 한다.
a = factory.returnCar("tomas")
b = factory.returnCar("tomas")

print(a)
print(b)
print(a==b)

