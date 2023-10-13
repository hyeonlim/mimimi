# 1-1
""" for i in range(1, 6):
    for j in range(6 -i):
        print("*", end="")
    print() """
    
""" for i in range(1, 6):
    print("*" * i) """

# 1-2
""" for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print() """

""" for i in range(5, 0, -1):
    print("*" * i) """
    
# 1-3
""" for i in range(1, 6):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """
    
# 1-4
""" for i in range(6, 0, -1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars) """


# 2-1
""" num = 0    
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """

# 2-2
""" num = 0   
line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = [] """

""" for i in range(5):
    num = i + 1
    line = [i + 1]
    for j in range(4):
        num += 5
        line.append(num)
    print(line)
    line = [] """

# 2-3
""" num = 26   
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """
    
# 가위, 바위, 보
import random

""" print("가위바위보~ 게임")
print("가위 = 1, 바위 = 2, 보 = 0")
user_choice = int(input("당신의 선택은?: "))
print(user_choice)

choices = [0, 1, 2]
computer_choice = random.choice
if user_choice == computer_choice:
    print("비겼습니다")
elif user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1 or user_choice == 0 and computer_choice == 2:
    print("이겼습니다")
else:
    print("졌습니다") """

""" def get_computer_choice():
    choices =  [1, 2, 3]
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("비겼습니다")
        return
    elif user_choice == 1 and pcnum == 0 or user_choice == 2 and pcnum == 1 or user_choice == 0 and pcnum == 2:
        print("이겼습니다")
        return
    else:
        print("졌습니다")
        return
    
print("가위바위보~ 게임")
print("가위 = 1, 바위 = 2, 보 = 0")
chnum = int(input("당신의 선택은?: "))
# pcnum = get_computer_choice()

determine_winner(chnum) """


# 파일 처리
# 파일 생성
# file = open("{경로 + 파일명.확장자}", "{파일권한 모드 설정 키워드}")

# 파일처리
# file.close()  # open and close is hanmom

# 쓰기 권한, 파일이 없으면 신규 생성
""" file = open("temp.txt", "w")

file.write("hello\n")
file.write("world\n")
file.write("Hi!")

file.close() """

""" file = open("C:\\Users\\Catholic\\temp.txt", "w")
for i in range(100):
    file.write(f"{ i }\n") 
file.close()"""

# 읽기 권한, 파일 없는데 열려하면 오류
""" file = open("temp.txt", "r")  
res = file.readlines()
print(res)
file.close() """
 
""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

res = file.read()
print(res)

file.close() """

# readline(s)
""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

for i in range(110):
    res = file.readline()
    print(res)

file.close() """

""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

res = file.readlines()
print(res)

file.close() """

""" file = open("C:\\Users\\Catholic\\temp.txt", "r")

line = file.readlines()
for l in line:
    print(l)
    
file.close() """

# 추가모드
""" file = open("temp.txt", "a")
file.close() """

""" file = open("C:\\Users\\Catholic\\temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close() """

# 읽기 및 쓰기 모드
""" file = open("temp.txt", "r+")
file.close() """

# 파일 객체로 읽기
""" file = open("C:\\Users\\Catholic\\temp.txt", "r")
for line in file :
	print(line)

file.close() """
