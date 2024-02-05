weather = "비"
if weather == "비": # = 은 2번 써야 해요!!
    print("우산을 챙기세요")

weather = "맑음" # 맑음으로 바꾸면 실행 안됨
if weather == "비":
    print("우산을 챙기세요")

weather = "미세먼지"
if weather == "비":
    print("우산을 챙기세요") # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요") # 2번

weather = "맑아요"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

weather = input("오늘 날씨는 어때요? ")
print(weather) # 사용자가 입력한 값 출력

weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리
if weather == "비" or weather == "눈": # 조건 변경
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")
