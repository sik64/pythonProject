# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("I eat %s apples." % "five")
    # #str = "I eat %s apples."
    # #num = "five"
    # # print(str % "five")
    # #print(str % num)
    #
    # #print(f"I eat {num} apples.")
    # number = 10
    # day = "three"
    # print("I ate %d apples. \nso I was sick for %s days." % (number, day))
    # print("%0.4f" % 3.141592)  # 3.1416
    # print("%.2f" % 3.141592)  # 3.14
    #
    # print("My num is {num1} and yours is {num2}".format(num1=3, num2=4))
    # print("My num is {0} and yours is {1}".format(3, 4))  # My num is 3 and yours is 4
    # print("{y:0.4f}".format(y=3.141592))  # 3.1416
    # age = 30
    # age2 = 20
    # print(f'나는 내년이면 {0}살이{1} 된다.', age, age2)
    # dic = {'name': '홍길동', 'age': 27}
    # print(f'나의 이름은 {dic["name"]}나이는 {dic["age"]}입니다.')
    # #나의 이름은 홍길동나이는 27입니다.
    # str = "string examples"
    # print(str.count('s')) # 2
    # print(str.find('t'))  # 1 # 처음으로 나오는 항의 인덱스만 출력
    # print(str.index('t'))  # 1 # 처음으로 나오는 항의 인덱스만 출력
    # print("_".join(str))  # s_t_r_i_n_g_ _e_x_a_m_p_l_e_s
    # print(str.upper()) # STRING EXAMPLES
    #
    # str = "STRING EXAMPLES"
    # print(str.lower()) # string examples
    # str.strip() # 양쪽 공백 지우기
    # str.lstrip() # 왼쪽 공백 지우기
    # str.rstrip()  # 오른쪽 공백 지우기
    #
    # print(str.replace("STRING", "PE")) # PE EXAMPLES # 문자열 바꾸기
    #
    # str =str.split(" ")
    # print(str) #['STRING', 'EXAMPLES'] #문자열을 나눈 후 배열로 반환

    list_a = [1, 2, ['a', 'b', ['Life', 'is']]]
    print(list_a[2][2][0])
    print(len(list_a))
    del list_a[2]
    print(list_a)  # [1, 2] # 리스트 요소 삭제
    list_a.append(4)  # [1, 2, 4] # 리스트 요소 추가 # 마지막 인덱스에 추가한다
    list_a.sort()  # 리스트 요소 정렬
    list_a.reverse()  # 리스트 역순으로 뒤집기
    list_a.insert(0, 4)  # [4, 1, 2, 4] # 0번 인덱스에 4 추가 # 리스트 삽입
    list_a.remove(4)  # [1 , 2, 4] # 첫 번째로 나오는 요소를 삭제
    list_a.pop()  # 리스르의 마지막 요소를 리턴하고 그 요소는 삭제한다
    list_a.count(1)  # 요소가 리스트 안에 몇개 있는지 계산 후 리턴
    list_a.extend([1, 2])  # 리스트 확장 # 인자로 리스트만 가능 리스트 더하기 개념

    # 튜플은 리스트와 비슷하지만 () 사용 , 수정 불가능이 차이점 이다.
    # 인덱싱, 슬라이싱 , 더하기 , 곱하기, 길이 구하기만 가능하다.

    # 딕셔너리
    # 딕셔너리는 Key와 Value로 리스트의 index에 이름을 지어준 것과 같다
    dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
    print(dic.keys())
    # 딕셔너리 dic에 keys만 모아 배열로 리턴한다.
    # dict_keys(['name', 'phone', 'birth'])
    print(list(dic.keys()))  # list로 형변환 해주면
    # ['name', 'phone', 'birth'] 로 리스트 처럼 이용가능하다.
    print(list(dic.items()))
    # Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
    # [('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')]

    print(dic.get('name'))  # pey
    print(dic["name"])  # pey

    # 딕셔너리 get() 과 index 방식의 차이
    # 값이 없을 경우 get()은 NONE을 반환하고 index방식은 에러가 난다.
    print(dic.get('address'))  # None
    print(dic.get('address'), '노노')  # 노노 # default값으로 '노노' 설정가능
    # print(dic["address"])  # error
    print('name' in dic)  # True # 딕셔너리 안의 key값 조사

    # 집합 자료형 set()
    # 집합 자료형은 키가 없는 딕셔너리와 같다
    # 중복이 없어지고 인덱싱이 불가능 하다
    # 합집합 , 교집합 , 차집합 사용시에 용이
    list_a = [1, 2, 3, 3, 4]
    set_a = set(list_a)
    print(set_a)  # {1, 2, 3, 4}

    list_b = [3, 4, 5, 6, 7]
    set_b = set(list_b)  # {1, 3, 4, 6, 7}
    print(set_a & set_b)  # 교집합 # {3, 4}
    print(set_a | set_b)  # 합집합 # {1, 2, 3, 4, 5, 6, 7}
    print(set_a - set_b)  # 차집합 # {1, 2}

    set_a.add(5)  # 집합에 값 추가
    print(set_a)  # {1, 2, 3, 4, 5}

    set_a.update([6, 7, 8])  # 집합에 여러 값 추가
    print(set_a)  # {1, 2, 3, 4, 5, 6, 7, 8}

    set_a.remove(1)  # 집합에서 값 삭제
    print(set_a)  # {2, 3, 4, 5, 6, 7, 8}

    # 불 연산
    # bool(값) 으로 값이 True 인지 False 인지 판단 가능
    # python 에서 True == 1 , False == 0

    a = [1, 2, 3, 4]
    while a:
        print(a.pop())
        # 리스트 a가 조건으로 들어가고 4번째 루프에서 리스트가 공백([])이 되므로 False값 (0) 을 리턴해서 조건이 닫히고 while문이 끝난다.

    b = a
    print(a == b)  # True
    print(a is b)  # True
    # 02-8 메모리 주소값으로 변수 생성하기 때문에 값은 같지만 다른 변수를 만들고 싶을 땐 [:] 또는 copy()함수를 사용해야 한다.
    print(id(a))  # 2524813377280
    print(id(b))  # 2524813377280
    a = [1, 2, 3, 4]
    b = a.copy()  #
    b = a[:]
    # 이렇게 복사할 시 a값을 변화시켜도 b값에 영향이 없다.
    print(id(a))  # 2524813376128
    print(id(b))  # 2524813377280
    # 진수 변환 코드
    # n진수 -> 10진수
    # 10진수 -> n진수 , bin(),oct(),hex()
    print(int('111', 2))  # 7
    print(int('222', 3))  # 26
    print(int('333', 4))  # 63
    print(int('444', 5))  # 124
    print(int('555', 6))  # 215
    print(int('FFF', 16))  # 4095


    # if 문 while 문

    # 사칙연산 클래스 만들기
    class FourCal:
        def __init__(self,first, second):  # a =FourCal(var1,var2) 로 생성시 전달해주어야 한다.
            self.first = first
            self.second = second
        def setdata(self, first, second):
            self.first = first
            self.second = second

        def add(self):
            return self.first + self.second
        def div(self):
            return self.first / self.second


    class MoreFourCal(FourCal):
        def pow(self):
            return self.first ** self.second
        def div(self):
            if self.second is not 0:
                return self.first / self.second
            else:
                return 0



    aa = MoreFourCal(2, 0)
    print(aa.pow())

    a = FourCal(3, 4)
    b = FourCal(5, 3)
    print(type(a))  # <class '__main__.FourCal'>
    a.first = 1
    a.second = 2

    print(a.first)
    print(b)
    print(type(b))
    # print(b.first) # error
    b.setdata(2, 3)
    print(b.first)
    print(a.first)
    print(a.second)
    print(a.add())

    print(aa.div())

    #pi = 3.141592 6535 8979 3238 4626 4338
