# score.txt 파일을 쓰기("w") 모드로 열기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기

# score.txt 파일을 쓰기("a") 모드로 열기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close()

# score.txt 파일을 읽기("r") 모드로 열기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 파일 전체 읽어오기
score_file.close()
