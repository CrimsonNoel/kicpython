# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:33:19 2023

@author: KITCOOP
"""
###########
# 클래스 : 사용자 정의 자료형
#         구조체+함수=> 변수+함수의 모임.
# 상속 : 다중 상속 가능. 여러개의 부모클래스가 존재.
# self : 자기참조변수, 인스턴트 함수의 매개변수로 설정해야함.
# 생성자 : def __init__(self
###########

class Car : # 기본생성자 제공 클래스 : 생성자를 구현하지 않음
    color = ""
    speed = 0
    def upSpeed(self,value):
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value

car1 = Car() #객체화
car1.color = "빨강"
car1.speed = 10

car2 = Car() #객체화
car2.color = "파랑"
car2.speed = 20
car2.upSpeed(30)
print("자동차1의 색상:%s, 현재 속도:%dKm" % (car1.color,car1.speed))
print("자동차2의 색상:%s, 현재 속도:%dKm" % (car2.color,car2.speed))

### 생성자 구현하기
class Car :
    color = ""
    speed = 0
    def __init__(self,v1,v2=0) : #생성자
        self.color = v1
        self.speed = v2
        
    def upSpeed(self,value):
        self.speed += value
    def downSpeed(self,value):
        self.speed -= value

car1 = Car("빨강",10) # 객체화, 생성자 호출
car2 = Car("파랑",20)

car3 = Car("노랑")

print("자동차1의 색상:%s, 현재 속도:%dKm" % (car1.color,car1.speed))
print("자동차2의 색상:%s, 현재 속도:%dKm" % (car2.color,car2.speed))
print("자동차3의 색상:%s, 현재 속도:%dKm" % (car3.color,car3.speed))

# 멤버변수 : 클래스 내부에 설정
# 인스턴스변수 : 객체별로 할당된 변수. self.변수명 형태
# 클래스 변수: 객체에 공통변수        클래스명.변수명 형태

class Car :
    color = "" # 색상
    speed = 0  # 속도
    num = 0    # 자동차번호
    count = 0  # 자동차객체 갯수
    def __init__(self,v1,v2=0) : #생성자
        self.color = v1  #인스턴스변수
        self.speed = v2  #인스턴스변수
        Car.count += 1   #클래스변수
        self.num = Car.count #인스턴스 변수
    def printMassage(self):
        print("색상:%s, 속도:%dkm, 번호:%d, 생산번호:%d" % \
              (self.color, self.speed, self.num, Car.count))

car1 = Car("빨강",10)
car1.printMassage() # 색상:빨강, 속도:10km, 번호:1, 생산번호:1
car2 = Car("파랑")
car1.printMassage() # 색상:빨강, 속도:10km, 번호:1, 생산번호:2
car2.printMassage() # 색상:파랑, 속도:0km, 번호:2, 생산번호:2

# 문제: Card 클래스 구현하기
#   멤버변수 : king(카드종류), number(카드숫자)
#             no(카드번호), count(현재까지 생성된 카드 갯수)
#   멤버함수 : printCard(), kind:heart, number:1, no:1, count:1

class Card : 
    kind =""
    number = 0
    no = 0
    count = 0
    def __init__(self, a="Spade",b=1):
        self.kind = a
        self.no = b
        Card.count += 1
        self.number = Card.count
    def printCard(self):
        print("kind: %s, number: %d, no:%d, count: %d" % \
              (self.kind, self.number, self.no, Card.count))



card1 = Card()
card1.printCard() # kind: Spade, number: 1, no:1, count: 1
card2 = Card("Heart")
card2.printCard() # kind: Heart, number: 2, no:1, count: 2
card3 = Card("Spade",10)
card1.printCard() # kind: Spade, number: 1, no:1, count: 3
card2.printCard() # kind: Heart, number: 2, no:1, count: 3
card3.printCard() # kind: Spade, number: 3, no:10, count: 3

# 상속 : 기존의 클래스를 이용하여 새로운 클래스 생성
#       다중상속이 가능
# class 클래스명(부모클래스1,부모클래스2,...)
class Car:
    speed = 0
    door = 3
    def upSpeed(self,v):
        self.speed += v
        print("현재 속도(부모클래스):%d" % self.speed)

# class sedan extends Car{} - Java
class Sedan(Car) : #Car 클래스를 상속.
        pass       #부모클래스와 동일
        
class Truck(Car) : #Car 클래스 상속
    def upSpeed(self, v): #오버라이딩
        self.speed += v
        if self.speed > 150:
            self.speed = 150
        print("현재 속도(자손클래스): %d" % self.speed)

car1 = Car()
car1.upSpeed(200) # 현재 속도(부모클래스):200
sedan1 = Sedan()
sedan1.upSpeed(200) # 현재 속도(부모클래스):200
truck1 = Truck()
truck1.upSpeed(200) # 현재 속도(자손클래스): 150

'''
클래스 : 멤버변수,멤버함수, 생성자.
           인스턴스변수 : self.변수명. 객체별로 할당되는 변수
           클래스변수   : 클래스명.변수명. 해당 클래스의 모든객체들의 공통변수
    self : 자기참조변수. 인스턴스함수에 첫번째 매개변수로 설정.
   생성자 : __init__(self,...) : 객체생성에 관여하는 함수
           클래스내부에 생성자가 없으면 기본생성자를 제공.        
   상속 : class 클래스명 (부모클래스명1,부모클래스명2,..) :
          다중상속가능           
          오버라이딩 : 부모클래스의 함수를 자손클래스가 재정의
'''

# 클래스에서 사용되는 특별한 함수
# __xxxx__ 형태인 함수.
class Line :
    length = 0
    def __init__(self,length):
        self.length = length
    def __repr__(self):         # 객체를 문자열로 출력
        return "선길이: "+str(self.length)
    def __add__(self,other):    # +연산자 사용시 호출
        print("+ 연산자 사용: ",end="")    
        return self.length + other.length
    def __lt__(self,other):     # <연산자 사용시 호출
        print("< 연산자 호출: ")        
        return self.length < other.length
    def __gt__(self,other):     #  >연산자 사용시 호출
        print("> 연산자 호출: ")  
        return self.length > other.length
    def __eq__(self,other):     #  ==연산자 사용시 호출
        print("== 연산자 호출: ")  
        return self.length == other.length
    
line1 = Line(200)
line2 = Line(100)
print("line1=",line1)
print("line2=",line2)
print("두선의 합: ",line1+line2)
print("두선의 합: ",line1.__add__(line2))
if line1 < line2:
    print("line2 선이 더 깁니다.")
elif line1 == line2:
    print("line1과 line2 선의 길이는 같습니다")
elif line1 > line2:
    print("line1 선이 더 깁니다.")
    
    
'''
클래스에서 사용되는 연산자에 사용되는 특수 함수
+   __add__(self, other)
–   __sub__(self, other)
*   __mul__(self, other)


/   __truediv__(self, other)
//   __floordiv__(self, other)
%   __mod__(self, other)
**   __pow__(self, other)
&   __and__(self, other)
|   __or__(self, other)
^   __xor__(self, other)
<   __lt__(self, other)
>   __gt__(self, other)
<=   __le__(self, other)
>=   __ge__(self, other)
==   __eq__(self, other)
!=   __ne__(self, other)

생성자 : __init__(self,...) : 클래스 객체 생성시 요구되는 매개변수에 맞도록 매개변수 구현
출력   : __repr__(self) : 클래스의 객체를 출력할때 문자열로 리턴.
'''

'''
    추상함수: 자손클래스에서 강제로 오버라이딩 해야 하는 함수
            함수의 구현부네 raise NotImplementedError
            를 기술
'''

class Parent:
    def method(self) : #추상함수
        raise NotImplementedError
        
class Child(Parent):
    #pass
    def method(self): #추상함수 오버랑딩
        print("자손클래스에서 오버라이딩함")
    
class Child2(Parent):
    pass

ch = Child()
ch.method()

ch2=Child2()
ch2.method()
































































































