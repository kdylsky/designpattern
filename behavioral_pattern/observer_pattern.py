"""
observer패턴 사용하기 전
강한 결합
"""
class Video:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
class Youtube:
    def __init__(self, Auser,Buser,Cuser):
        self.Auser = Auser
        self.Buser = Buser
        self.Cuser = Cuser
        self.video = None

    def newvideo(self, video):
        self.video = video
        self.Auser.update(video)
        self.Buser.update(video)
        self.Cuser.update(video)

class Auser:
    def update(self, video):
        print("Auser 영상알림")

class Buser:
    def update(self, video):
        print("Buser 영상알림")

class Cuser:
    def update(self, video):
        print("Cuser 영상알림")


# test_video = Video("안녕", "반가워")
# a = Auser()
# b = Buser()
# c = Cuser()
# test_youtube = Youtube(a,b,c)
# test_youtube.newvideo(test_video)

"""
이 경우라면, 주체(Youtube)에 직접 객체들을 등록해주어야 한다. 또한 객체가 늘어나는 경우 주체(Youtube)를 바꾸어 주어야한다.
또한 새로운 변경이 일어나는 이벤트(newvideo)가 실체구현체(update()메서드)를 알고 있어야 한다.
"""







from abc import ABC, abstractmethod
"""
느슨한 결합
인터페이스를 이용해서 객체간의 관계를 느슨하게 한다. 
하지만 객체 하나에 대해서만 알림을 줄수 있다.
"""
class Video:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    

class Youtube:
    def __init__(self, observer):
        self.observer = observer

    def newvideo(self, video):
        self.observer.update(video)

class Observer(ABC):
    def update(self, video):
        pass

class Auser(Observer):
    def update(self, video):
        print("Auser 영상알림")

class Buser:
    def update(self, video):
        print("Buser 영상알림")

class Cuser:
    def update(self, video):
        print("Cuser 영상알림")

# a = Auser()
# b = Buser()
# c = Cuser()
# v = Video("안녕", "반가워")

# test = Youtube(a)
# test.newvideo(v)







"""
옵저버패턴
푸시방식
"""
class Video:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Observer(ABC):
    def update(self, video):
        pass

class Auser(Observer):
    def update(self, video):
        print("Auser 영상알림")

class Buser(Observer):
    def update(self, video):
        print("Buser 영상알림")

class Cuser(Observer):
    def update(self, video):
        print("Cuser 영상알림")


class Subject(ABC):
    def attach(self,observer):
        pass
    def detach(self,observer):
        pass
    def notifyobserver(self):
        pass


class Youtube(Subject):
    def __init__(self, observers = []):
        self.observers = observers
        self.video = None

    def attach(self,observer):
        self.observers.append(observer)
    def detach(self,observer):
        self.observers.remove(observer)
    def notifyobserver(self):
        for observer in self.observers:
            observer.update(self.video)
    
    def newvideo(self, video):
        self.video = video
        self.notifyobserver()




"""
옵저버
pull방식
"""

class Video:
    def __init__(self, title, content, language):
        self.title = title
        self.content = content
        self.language = language


class Observer(ABC):
    def update(self, subject,language):
        pass

class Auser(Observer):
    def update(self, subject,language):
        print(f"Auser {language} 영상알림")

class Buser(Observer):
    def update(self, subject, language):
        if language == "python":
            print(f"Buser {language} 영상알림")

class Cuser(Observer):
    def update(self, subject, language):
        if language == "java":
            print(f"Cuser {language} 영상알림")


class Subject(ABC):
    def attach(self,observer):
        pass
    def detach(self,observer):
        pass
    def notifyobserver(self):
        pass


class Youtube(Subject):
    def __init__(self, observers = []):
        self.observers = observers
        self.video = None
        self.language = ""

    def attach(self,observer):
        self.observers.append(observer)
    
    def detach(self,observer):
        self.observers.remove(observer)
    
    def notifyobserver(self):
        for observer in self.observers:
            observer.update(self.video, self.language)
    
    def newvideo(self, video):
        self.video = video
        self.language = video.language
        self.notifyobserver()


a = Auser()
b = Buser()
c = Cuser()
v = Video("안녕","반가워","java")

test = Youtube()
test.attach(a)
test.attach(b)
test.attach(c)

test.newvideo(v)















# class SaleObserver(ABC):
#     def update(self, subject):
#         pass

# class Amart(SaleObserver):
#     def __init__(self, appleprice, bananaprice, grapeprice):
#         self.APPLE = "apple"
#         self.BANANA = "banana"
#         self.GRAPE = "grape"
#         self.appleprice = appleprice
#         self.bananaprice = bananaprice
#         self.grapeprice = grapeprice

#     def update(self, subject):
#         self.appleprice = subject.getPrice(self.APPLE)
#         self.bananaprice = subject.getPrice(self.BANANA)
#         self.grapeprice = subject.getPrice(self.GRAPE)
    

#     def __str__(self):
#         return f"Amart의 apple :{self.appleprice}, banan :{self.bananaprice}, grape:{self.grapeprice}"


# class Bmart(SaleObserver):
#     def __init__(self, appleprice):
#         self.APPLE = "apple"
#         self.appleprice = appleprice
        
#     def update(self, subject):
#         self.appleprice = subject.getPrice(self.APPLE)

#     def __str__(self):
#         return f"Bmart의 apple :{self.appleprice}"

# class Cmart(SaleObserver):
#     def __init__(self, bananaprice, grapeprice):
#         self.BANANA = "banana"
#         self.GRAPE = "grape"
#         self.bananaprice = bananaprice
#         self.grapeprice = grapeprice

#     def update(self, subject):
#         self.bananaprice = subject.getPrice(self.BANANA)
#         self.grapeprice = subject.getPrice(self.GRAPE)
    

#     def __str__(self):
#         return f"Cmart의 banan :{self.bananaprice}, grape:{self.grapeprice}"




# class Subject(ABC):
#     def addObserver(self, observer):
#         pass

#     def removerObserver(self, observer):
#         pass

#     def notificationObserver(self):
#         pass

#     def getPrice(self, name):
#         pass


# class Sale(Subject):
#     def __init__(self, sale = {}, observers = []):
#         self.sale = sale
#         self.observers = observers

#     def updatePrice(self, name, price):
#         self.sale[name] = price
#         self.notificationObserver()
    
#     def addObserver(self, observer):
#         self.observers.append(observer)

#     def removerObserver(self, observer):
#         self.observers.remove(observer)

#     def notificationObserver(self):
#         for observer in self.observers:
#             observer.update(self)

#     def getPrice(self, name):
#         if name in self.sale:
#             return self.sale.get(name)
        
# sales = Sale()

# amart = Amart(500, 10, 1)
# bmart = Bmart(10)
# cmart = Cmart(10,1)

# print(amart)
# print(bmart)
# print(cmart)

# sales.addObserver(amart)
# sales.addObserver(bmart)
# sales.addObserver(cmart)


# sales.updatePrice("apple", 10000)

# print(amart)
# print(bmart)
# print(cmart)

