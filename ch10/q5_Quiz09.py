# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#        출력 메세지 : "잘못된 값을 입력하였습니다."

# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#        출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

class SoldOutError(Exception): # 사용자 정의 에러 (재고 소진)
    pass

chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

while(True):
    try: # try 구문 추가
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        elif order <= 0: # 입력값이 1보다 작은 수일 때
            raise ValueError    
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1 # 대기번호 증가
            chicken -= order # 주문 수 만큼 남은 치킨 감소

        if chicken == 0: # 남은 치킨 수가 0 이면
            raise SoldOutError # 더 이상 주문 불가하므로 재고 소진 에러 발생
        
    except ValueError: # ValueError 처리 추가
        print("잘못된 값을 입력하였습니다.")
        
    except SoldOutError: # 재고 소진 에러 처리
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break # while 반복문 탈출
