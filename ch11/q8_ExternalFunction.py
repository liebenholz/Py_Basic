import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# -----------------------------------
import os
print(os.getcwd()) # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder): # 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
else: # 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
    
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")
    
print(os.listdir())

# -----------------------------------
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초

# -----------------------------------
import datetime
print("오늘 날짜는", datetime.date.today())

today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후