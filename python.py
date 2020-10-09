# import theather_module
# theather_module.price(3)
# theather_module.price_mornig(4)
# theather_module.price_soldier(5)

# import theather_module as mv
# mv.price_soldier(3)
# mv.price_mornig(5)
# mv.price(10)

# from theather_module import *
# price(3)
# price_mornig(5)
# price_soldier(3)

# from theather_module import price, price_mornig
# price(5)
# price_mornig(10)

# from theather_module import price_soldier as price
# price(4)

# import traval.tal
# trip_to = traval.tal.ThailandPackage()
# trip_to.detail()

# from traval.tal import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from traval import vat
# trip_to = vat.VietnamPackage()
# trip_to.detail()

# from traval import *
# trip_to = tal.ThailandPackage()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random)) #랜덤 모듈의 위치 출력
# print(inspect.getfile(tal))


# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())

# import pickle
# print(dir())

# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

# name = "Lee"
# print(dir(name))

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 있는 폴더")
#     os.rmdir(folder)
#     print(folder, "폴더 삭제")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더 생성")
# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# # print("오늘 날짜는 ", datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("현재부터 100일 후는", today + td)

import inspect
import byme
print(inspect.getfile(byme))
byme.sign()


