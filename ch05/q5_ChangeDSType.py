menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # menu 의 type 정보 : set

menu = list(menu)       # 리스트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : list

menu = tuple(menu)      # 튜플 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : tuple

menu = set(menu)        # 세트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : set