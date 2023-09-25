# datetime: 날짜와 시간을 다루는 함수를 제공
""" from datetime import datetime as dt """

# 현재시간출력
""" print(dt.now()) """

# 특정 시간대의 현재시간 출력
""" from pytz import timezone
# tz = timezone('Asia/Seoul')
tz = timezone('UTC')
print("timezon : ", dt.now(tz)) """ # pip 없어서 실행안 됨

# 문자열을 날짜로 변환
""" date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object) """

# 날짜를 문자열로 변환
""" date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """

# 모듈화
""" import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res) """


# OS

""" import os

# 현재 디렉토리 출력
print(os.getcwd())

# 상위 디렉토리로 변경, 상대경로, 절대경로
os.chdir("../")
# 변경된 디렉토리 출력
print(os.getcwd())

# 파일목록 출력 
print(os.listdir())

# 폴더 삭제 
os.rmdir("new_directory")

# 폴더 생성 
os.mkdir("new_directory")
print(os.listdir())
 """
#  모듈화
""" import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir()) """  # 리무브파일


# sys : Python 인터프리터와 상호작용하기 위한 함수를 제공
import sys

# 버전정보 출력
print(sys.version)

# 명령 인수 확인
print(sys.argv)



# 스택(Stack) 후입선출(LIFO : Last In First Out)
""" st = []

# 값넣기
st.append(1)
st.append(2)
st.append(3)
st.append(4)
st.append(5)

# 스텍의 상태확인
print(st)

# 스택에서 값빼기
top = st.pop()
print(top)
print(st)
print(len(st)) """

# 큐(Queue) 선입선출(First In First Out)
""" queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

front = queue.pop(0)
print(front)
print(queue)
print(len(queue)) """

