# print(2**3) # 제곱
# print(5%3)
# print(abs(-5)) # 5
# print(pow(4, 2)) # 16
# print(max(5, 12)) # 12
# print(round(3.14)) # 3

# from math import *
# print(floor(4.99)) # 4
# print(ceil(3.14)) # 4
# print(sqrt(16)) # 4 (제곱근)

from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)

# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


# day = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 {} 일로 선정되었습니다".format(day))
# print(randint(0, 2))
# print(randint(0, 2))
# print(randint(0, 2))

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) # 대문자 여부 감지
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n") # n의 위치 반환
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))

# # print(python.index("Java"))
# print(python.count("n"))
# print("a" + "b")
# print("a", "b")
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요" % "파이썬")
# print("Apple은 %c로 시작해요" % "A")

# print("나는 {1}색과 {0}색을 좋아해요".format("파랑", "빨강"))
# print("나는 {color}}색과 {age}색을 좋아해요".format(age = "20", color = "빨강"))
# age = 20
# color = "빨강"
# # print(f"나는 {color}색과 {age}살을 좋아해요") #v 3.7 이상부터 사용 가능

# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '이재현'입니다.")
# print("저도 \"이재현\"입니다.")

# print("C:\\Users\\ainos\\OneDrive\\Desktop\\Python_workspace")
# print("Red Apple\rpine")
# print("Redd\bApple")
# print("Red\tApple")


# add = "http://naver.com"
# add1 = add[7:12]
# print(add1)
# add2 = len(add1)
# add3 = add1.count('e')
# print('{}{}{}{}'.format(add1,add2,add3,"!"))

# subway = [10, 20, 30]
# print(subway)

# subway = ['유재석', '조세호', '박명수']
# print(subway)

# print(subway.index("조세호"))

# # 맨 뒤에 추가
# subway.append("하하")
# print(subway)

# # 위치 지정 후 추가
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway.pop())
# print(subway.pop())

# print(subway)

# subway.append("유재석")
# print(subway.count("유재석"))

# # asc 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용 가능
# num_list = [5,4,3,2,1]
# mix_list = ["조세호", 20, True]
# num_list.extend(mix_list) # 리스트 합침
# print(num_list)


# cabinet = {3:"유재석", 100:"김태호"}
# # print(cabinet[3])


# # print(cabinet.get(3))

# # # print(cabinet[5]) # 없으므로 프로그램 종료됨
# # print(cabinet.get(5, "사용 가능"))

# # print(3 in cabinet) # true
# # print(5 in cabinet) # false

# # # 사전에 키 추가
# # cabinet["c-20"] = "조세호"
# # print(cabinet["c-20"])

# # del cabinet["c-20"]
# # print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items()) # key, value 쌍으로 출력
# print(cabinet)

# cabinet.clear()
# print(cabinet)


# menu = ("돈가스", "치즈까스") # 튜플은 add 안됨
# menu.add('생선까스')
# print(menu[0])
# print(menu[1])

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# my_set = {1,2,3,3,3} # 집합(set)은 중복 안됨
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(['유재석', '박명수'])

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집합
# print(java | python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)
# python.remove("유재석")


#자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# import random
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


# samplelist = random.sample(list, 4)
# samplelist2 = samplelist.pop()

# print(samplelist2, samplelist)

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")
# else:
#     print("준비물 없음")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("개더움")
# elif 10 <= temp and temp < 30:
#     print("ㄱㅊ")
# elif 0 <= temp < 10:
#     print("개춥")
# else:
#     print("ㅈㄴ 추움")

# for waiting_no in range(1, 6):
#     print("대기번호 : {}".format(waiting_no))

# starbucks = ["iron", "tor", "grout"]
# for customer in starbucks:
#     print("{}, 커피가 준비되었습니다".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{}, 커피가 준비 되었습니다 {}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다")



# customer = "아이언맨"
# index = 1
# while True:
#     print("{}, 커피가 준비 되었습니다 {}번 불렀어요".format(customer, index))
#     index += 1
    

# customer = "토르"
# person = "unknown"

# while person != customer:
#     print("{}, 커피가 준비되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요?")


# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("수업 끝, {}는 교무실로 따라와".format(student))
#         break
#     print("{}, 책 읽어".format(student))

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

students = ['Iron man', 'thor', 'groot']
students = [len(i) for i in students]
print(students)


















































