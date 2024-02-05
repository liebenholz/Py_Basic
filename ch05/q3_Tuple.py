# Tuple : read only of List
# (value1, value2, ...)

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩