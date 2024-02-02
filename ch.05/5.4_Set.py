# Set : no duplication, no index
# {value1, value2, ...}

my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않으므로 3은 1번만 들어감
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"} # 자바 개발자 집합
python = set(["유재석", "박명수"]) # 파이썬 개발자 집합

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)             # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 또는 python 을 할 수 있는 개발자)
print(java | python)        # {'박명수', '유재석', '김태호', '양세형'}
print(java.union(python))   # {'박명수', '유재석', '김태호', '양세형'}

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)            # {'양세형', '김태호'}
print(java.difference(python))  # {'양세형', '김태호'}

# python 개발자 추가 (기존 개발자 : 박명수, 유재석)
python.add("김태호")
print(python)       # {'박명수', '유재석', '김태호'}

# java 개발자 삭제 (기존 개발자 : 유재석, 김태호, 양세형)
java.remove("김태호")
print(java)         # {'유재석', '양세형'}

# output results may change because "Set" has no index