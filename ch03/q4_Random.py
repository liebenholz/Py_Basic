# random 모듈에서 모든 것들을 가져다 쓰겠다는 의미
from random import *

print(random())                 # 0.0 이상 1.0 미만의 임의의 값 생성

print(random() * 10)            # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10))       # 0 이상 10 미만의 임의의 정수 값 생성
print(int(random() * 10) + 1)   # 1 이상 10 이하 (11 미만) 의 임의의 정수 값 생성

# 로또 번호 뽑기
print(int(random() * 45) + 1)   # 1 이상 46 미만의 임의의 정수 값 생성
print(randrange(1, 46))         # 1 이상 46 미만의 임의의 정수 값 생성
print(randint(1, 45))           # 1 이상 45 이하(45를 포함!!)의 임의의 정수 값 생성