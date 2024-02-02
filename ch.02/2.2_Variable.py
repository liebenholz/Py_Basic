# 애완동물을 소개합니다.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age > 3

print("우리집 " + animal + "의 이름은 " + name + "에요.")
# print(name + "는 " + str(age) + "살이고 " + hobby + "을 좋아한답니다.")
# "+"가 아니라 ","로 변수들을 연결할 경우 뒤에 " "이 들어간다는 것을 유의할 것
print(name, "는 ", age,"살이고 ", hobby, "을 좋아한답니다.")
print(name + "는 어른일까요? : " + str(is_adult))

# 주석 사용하는 방법
'''
이렇게 하면
헤당 영역은
주석처리가 됩니다
'''

# 혹은 일괄선택 후 'ctrl + /'
# print("우리집 " + animal + "의 이름은 " + name + "에요.")
# print(name + "는 " + str(age) + "살이고 " + hobby + "을 좋아한답니다.")
# print(name + "는 어른일까요? : " + str(is_adult))