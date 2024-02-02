# List : has index, allows duplication

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호")) # 1 (인덱스는 0부터 시작)

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈씨를 유재석 / 조세호 사이에 태움
subway.insert(1, "정형돈") # 인덱스 1 위치에 삽입
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄, 후입선출
print(subway.pop()) # 하하 내림
print(subway) # ['유재석', '정형돈', '조세호', '박명수']
print(subway.pop()) # 박명수 내림
print(subway) # ['유재석', '정형돈', '조세호']
print(subway.pop()) # 조세호 내림
print(subway) # ['유재석', '정형돈']

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석") # 설명을 위해 유재석씨를 맨 뒤에 태울게요
print(subway) # ['유재석', '정형돈', '유재석']
print(subway.count("유재석")) # 유재석씨가 2명이 있네요!