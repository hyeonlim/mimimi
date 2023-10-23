# import os

# fp = "temp.txt"

# file = open(fp, "w")

""" if os.path.exists(fp):
    print("ok")
    file = open("temp.txt", "a")
else:
    print("error")
    file = open("temp.txt", "w") """
    
""" if os.path.exists(fp):
    f = open(fp, "r")
    for line in f:
        print(line)
        
else:
    f = open(fp, "w")
    for i in range(100):
        f.write(str(i) + "\n")
        
f.close() """


# 파일 생성 및 삭제 확인
""" def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)
        

fp = "new.txt"

f = open(fp, "w")
f.close()

os.remove(fp)
print("----------------------------\n\n")
dir_print("./")
# print("complete") """

# 파일명 변경
""" import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.rename(fp, "new1.txt")
print("complete") """

# 재변경 예외처리
""" import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

if os.path.exists(tp):
    print("exist, same name file")
    os.rename(tp)
else:
    os.rename(fp, "new1.txt")
    print("complete") """
    
# 파일명 변경 확인
""" import os 

def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp, "w")
f.close()

dir_print("./")
print("\n===============================\n\n")

if os.path.exists(tp):
    os.rename(tp)
    dir_print("./")
    print("exist, same name file")
else:
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete") """
    
# with
""" 
# f = open("temp.txt", "r")
with open("temp.txt", "r") as f:
    print(f.read())
    
    # for i in range(110):
        # res = f.readline()
        # print(res) """



# 네트워크
""" 데이터 전송 원리
데이터 전송은 쪼개져서 보내짐. 네크워크 어뎁터 = nic 라는 내부버퍼 통해 분화, 패킷화
"""

        