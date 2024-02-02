# 1. 읽으려는 줄이 있는 동안 계속 반복하여 읽어들이도록
score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄바꿈 중복을 방지하기 위해 end="" 처리
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어올 내용이 없으면?
        break # 반복문 탈출
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()


# 2. 리스트에 저장해두고 리스트를 반복 순회
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()