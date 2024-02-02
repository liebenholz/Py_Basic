def open_account():
    print("새로운 계좌가 생성되었습니다.")
    
def deposit(balance, money): #입금
    print("입금이 완료되었습니다, 잔액은 {0}원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다, 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:   # 잔액이 출금보다 적으면
        print("잔고가 부족하여 출금이 완료되지 않았습니다, 잔액은 {0}원입니다.".format(balance))
        return balance
    
def withdraw_night(balance, money): # 영업외 시간 출금
    commission = 100    # 수수료
    
    if balance >= money + commission:
        print("출금이 완료되었습니다, 잔액은 {0}원입니다.".format(balance-money-commission))
        return commission, balance - money - commission
    else:
        print("잔고가 부족하여 출금이 완료되지 않았습니다, 잔액은 {0}원입니다.".format(balance))
        return commission, balance
        
balance = 0
balance = deposit(balance, 1000)
# print(balance)

#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)

print("수수료는 {0}원, 잔액은 {1}원입니다.".format(commission, balance))