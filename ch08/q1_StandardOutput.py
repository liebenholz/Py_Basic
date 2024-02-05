print("Python", "Java")
print("Python" + "Java")

print("Python", "Java", sep=",") # 값들을 (,)로 구분
print("Python", "Java", "JavaScript", sep=" vs ") # 값들을 "vs" 로 구분

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys # sys 모듈을 가져와서 사용하겠다는 의미
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
scores = {"수학" : 0, "영어":50, "코딩":100}
for subject, score in scores.items(): # key, value
    #print (subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표 
# 001, 002, 003, ..
for num in range(1, 21):
    #print("대기번호 : " + str(num))
    print("대기번호 : "+ str(num).zfi11(3))