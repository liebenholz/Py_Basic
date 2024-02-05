class Unit:
    def __init__(self, name, hp, damage): # 3개의 전달값
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine3 = Unit("마린") # 전달값 3개 중 1개만 넘김
# TypeError: __init__() missing 2 required positional arguments: 'hp' and 'damage'

marine4 = Unit("마린", 40) # 전달값 3개 중 2개만 넘김
# TypeError: __init__() missing 1 required positional argument: 'damage'

# 클래스 객체를 생성할 때는 __init__() 생성자에 정의된 self 를 제외한 갯수만큼 전달값을 넘겨줘야 함.ㅌㅈ