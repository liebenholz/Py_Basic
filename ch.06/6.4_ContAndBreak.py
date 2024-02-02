absent = [2, 5] # 결석한 학생 출석번호

for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    print("{0}, 책을 읽어봐".format(student))

absent = [2, 5] # 결석한 학생 출석번호
no_book = [7] # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    elif student in no_book: # 책을 가져오지 않았으면 바로 수업 종료 (반복문 탈출)
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))