try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
    
# 입력된 값이 정수가 아님
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

# 0으로 나누기 불가
except ZeroDivisionError as err:
    print(err)

# 그 외 추가적인 에러
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)