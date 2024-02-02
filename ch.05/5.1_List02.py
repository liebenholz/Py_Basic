num_list = [5, 2, 4, 3, 1]

num_list.sort()     # 오름차순 정렬
print(num_list)     # [1, 2, 3, 4, 5]

num_list.reverse()  # 순서 뒤집기
print(num_list)     # [5, 4, 3, 2, 1]

num_list.clear()    # 모두 지우기
print(num_list)     # []

mix_list = ["조세호", 20, True] # 다양한 자료형을 함께 사용 가능
print(mix_list)               # ['조세호', 20, True]

num_list = [5, 2, 4, 3, 1]  # num_list 값 다시 정의
num_list.extend(mix_list)   # 리스트 확장
print(num_list)             # [5, 2, 4, 3, 1, '조세호', 20, True]