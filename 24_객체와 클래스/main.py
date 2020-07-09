# 클래스 : 객체를 만들기 위한 설계도
class TestClass1:
    pass

# 클래스를 이용해 객체를 생성한다.
t1 = TestClass1()
t2 = TestClass1()
print(f't1 : {t1}')
print(f't2 : {t2}')
print(f't1 type: {type(t1)}')
print(f't2 type: {type(t2)}')

# 파이썬은 생성된 객체에 변수를 추가하는 것이 자유롭다.
# 객체가 가지고 있는 변수나 함수를 멤버라고 부른다.
# . 연산자를 이용하면 객체가 가지고 있는 멤버에 접근할 수 있다.
# 만약 값을 넣어주는 코드를 작성했는데 해당 멤버가 없다면 추가해준다.
t1.v1 = 100
t1.v2 = '안녕하세요'
print(f't1.v1 : {t1.v1}')
print(f't1.v2 : {t1.v2}')


# 생성자 함수 :
class TestClass2 :
    # 클래스를 통해 객체가 생성된 후에 자동으로 호출되는 함수
    # 클래스에 정의한 모든 함수는 첫 번째 매개변수로 self를 갖고있다.
    # self에는 함수를 호출 할 떄 사용한 객체가 들어온다.
    # init의 경우 생성된 객체가 들어온다.
    def __init__(self):
        print('__init__호출')
        # 객체에 변수를 추가한다.
        self.v1 = 100
        self.v2 = 200

t3 = TestClass2()
t4 = TestClass2()
print(f't3.v1 : {t3.v1}')
print(f't3.v2 : {t3.v2}')
print(f't4.v1 : {t4.v1}')
print(f't4.v2 : {t4.v2}')

# 각 객체가 가지고 있는 변수는 객체마다 따로 따로 생성되어 관리되기
# 때문에 독립적이다!

class TestClass3():

    def __init__(self, a1, a2):
        self.v1 = a1
        self.v2 = a2

#객체를 생성할 때 전달하는 값은 init 함수로 전달된다.
t5 = TestClass3(100, 200)
t6 = TestClass3(1000, 2000)
print(f't5.v1 : {t5.v1}')
print(f't5.v2 : {t5.v2}')
print(f't6.v1 : {t6.v1}')
print(f't6.v2 : {t6.v2}')

#메서드들은 반드시 객체를 통해서 호출해야한다.
class TestClass4 :
    # init 메서드
    def __init__(self, a1, a2):
        print('init 메서드')
        self.v1 = a1
        self.v2 = a2

    # 인스턴스 메서드
    def f1(self):
        print('f1 호출')
        print(f'v1 : {self.v1}')
        print(f'v2 : {self.v2}')

t10 = TestClass4(100,200)
t11 = TestClass4(1000,2000)

#t10이라는 객체를 이용해서 F1을 출력
t10.f1()
t11.f1()
