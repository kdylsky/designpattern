"""
추상팩토리
"""
from abc import ABC, abstractmethod


# 팩토리의 상위클래스로 하위클래스(팩토리)가 어떤 동작을 하는지 큰 틀을 잡는다.
class RobotFactory(ABC):
    @abstractmethod
    def create_dog_robot(self):
        pass

    @abstractmethod
    def create_bird_robot(self):
        pass

# 하위클래스에서 실제 어떤 동작을 하는지 정의한다.
# A팩토리의 하나의 세트를 만든다.
class ARobotFactory(RobotFactory):
    def create_dog_robot(self):
        return BigDog()
    
    def create_bird_robot(self):
        return SlowBird()


# B팩토리의 하나의 세트를 만든다.
class BRobotFactory(RobotFactory):
    def create_dog_robot(self):
        return SmallDog()
    
    def create_bird_robot(self):
        return FastBird()



class Dog(ABC):
    @abstractmethod
    def bark(self):
        pass

class BigDog(Dog):
    def bark(self):
        print("bigdog bark")

class SmallDog(Dog):
    def bark(self):
        print("smalldog bark")


class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FastBird(Bird):
    def fly(self):
        print("fastbird fly")

class SlowBird(Bird):
    def fly(self):
        print("slowbird fly")












class User:
    def __init__(self, username):
        self.username = username
    
class Product:
    def __init__(self, productname):
        self.productname = productname


    

class UserModel(ABC):    
    def insertUserinfo(self, user):
        pass
    def updateUserinfo(self, user):
        pass
    def deleteUserinfo(self, user):
        pass

class MysqlUser(UserModel):
    def insertUserinfo(self, user):
        pass
    def updateUserinfo(self, user):
        pass
    def deleteUserinfo(self, user):
        pass

class OracleUser(UserModel):
    def insertUserinfo(self, user):
        pass
    def updateUserinfo(self, user):
        pass
    def deleteUserinfo(self, user):
        pass


class ProductModel(ABC):
    def insertProduct(self, product):
        pass
    def updateProduct(self, product):
        pass
    def deleteProduct(self, product):
        pass


class MysqlProduct(ProductModel):
    def insertProduct(self, product):
        pass
    def updateProduct(self, product):
        pass
    def deleteProduct(self, product):
        pass

class OracleProduct(ProductModel):    
    def insertProduct(self, product):
        pass
    def updateProduct(self, product):
        pass
    def deleteProduct(self, product):
        pass



class BigFactory(ABC):
    def createUserInfoDao(self):
        pass
    def createProductDao(self):
        pass

class OracleFactory(BigFactory):
    def createUserInfoDao(self):
        pass    
    def createProductDao(self):
        pass













class Userinfo:
    def __init__(self, userid, password, username):
        self.__userid = userid
        self.__password = password
        self.__username = username
    
    @property
    def userid(self):
        return self.__userid
    
    @property
    def password(self):
        return self.__password
    @property
    def username(self):
        return self.__username
    
    @userid.setter
    def userid(self, userid):
        self.__userid = userid

    @password.setter
    def password(self, password):
        self.__password = password

    @username.setter
    def username(self, username):
        self.__username = username


class Product:
    def __init__(self, productid, productname):
        self.__productid = productid
        self__productname = productname

    @property
    def productid(self):
        return self.__productid
    
    @property
    def productname(self):
        return self.__productname
    
    @productid.setter
    def productid(self, productid):
        self.__productid = productid

    @productname.setter
    def productname(self, productname):
        self.__productname = productname


# 쿼리문이 sql마다 다르다.
# 상위클래스에서는 inset, delete, updata 등의 기능을 할것이라는 것을 정의해주고
# 하위클래스 mysql, 오라클에서 각 sql에 맞게 쿼리문을 작성해준다.
class UserInfoDao(ABC):    
    def insertUserinfo(self, user):
        pass
    def updateUserinfo(self, user):
        pass
    def deleteUserinfo(self, user):
        pass

class UserMysqlDao(UserInfoDao):
    def insertUserinfo(self, user):
        print(f"mysql Dao {user.userid}")
        
    def updateUserinfo(self, user):
        print(f"mysql Dao {user.userid}")
        
    def deleteUserinfo(self, user):
        print(f"mysql Dao {user.userid}")
            
class UserOracleDao(UserInfoDao):
    def insertUserinfo(self, user):
        print(f"Oracle Dao {user.userid}")
        
    def updateUserinfo(self, user):
        print(f"Oracle Dao {user.userid}")
        
    def deleteUserinfo(self, user):
        print(f"Oracle Dao {user.userid}")
            



class ProductDao(ABC):
    def insertProduct(self, product):
        pass
    def updateProduct(self, product):
        pass
    def deleteProduct(self, product):
        pass

class ProductMysqlDao(ProductDao):
    def insertProduct(self, product):
        print(f"mysql Dao {product.productid}")
        
    def updateProduct(self, product):
        print(f"mysql Dao {product.productid}")
        
    def deleteProduct(self, product):
        print(f"mysql Dao {product.productid}")
            

class ProductOracleDao(ProductDao):
    def insertProduct(self, product):
        print(f"oracle Dao {product.productid}")
    
    def updateProduct(self, product):
        print(f"oracle Dao {product.productid}")
        
    def deleteProduct(self, product):
        print(f"oracle Dao {product.productid}")
        
# 상위팩토리에서 팩토리들이 하는 일을 나여한다.
class DaoFactory(ABC):
    def createUserInfoDao(self):
        pass
    
    def createProductDao(self):
        pass
    

class OracleFactory(DaoFactory):
    def createProductDao(self):
        return ProductOracleDao()

    def createUserInfoDao(self):
        return  UserOracleDao()

class MysqlFactory(DaoFactory):
    def createUserInfoDao(self):
        return UserMysqlDao()
    
    def createProductDao(self):
        return ProductMysqlDao()







