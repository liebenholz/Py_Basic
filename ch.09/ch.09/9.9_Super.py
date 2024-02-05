# 부모 클래스의 이름을 직접 적지 않고도 부모 클래스에 접근하는 방법
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 순서 변경
    def __init__(self):
        # super().__init__()
        # 순서상 가장 먼저 상속받은 클래스로 접근
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출

# 드랍쉽
dropship = FlyableUnit()