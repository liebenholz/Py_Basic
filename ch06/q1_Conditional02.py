temp = int(input("기온은 어때요? "))

if 30 <= temp: # 30 도 이상이면
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# 위 비교 문장은 이렇게도 작성 가능합니다.
# elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: # 그 외의 모든 경우 (0도 미만이면)
    print("너무 추워요. 나가지 마세요")