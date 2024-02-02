print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에는 waiting_no 의 값이 들어가요

for waiting_no in range(5): # 0부터 5직전까지 (0~4)
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1부터 6직전까지 (1~5)
    print("대기번호 : {0}".format(waiting_no))