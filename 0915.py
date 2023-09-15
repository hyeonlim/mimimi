# 식별연산
""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  
 """

""" a = 5
b = 5

print(a is b)
print(a is not b) """

""" a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b)

print(3 == 3.0)
print(3 is 3.0) """

""" a = [3 , 5, 1]
b = a
print(a is b)
a[0] = 2
print(a, b)
print(a is b) """

# a = 2 + 3 * 4
# a = 10 / 5 / 2
# a = 2 ** 3 ** 2
# a = 2 ** (3 ** 2)
# a = 10 % 3 % 2
# a = 1 + 2 > 3
# a = 4 - 1 < 2
# a = not False and True
# a = not True or False and True
# a = 1 & 2 | 3 ^ 4
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# a = 2 * -3 // 2
# a = 1 == 2 != 3
# print(a)


# 조건문
# if예시
""" x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero") """
    
# 짝홀 구분
""" num = 23
if num % 2 == 0:
    print("짝~수!")
else:
    print("홀~수!") """
    
# 두 수 비교
""" a = 5
b = 8

if a == b:
    print("a는 b와 같습니다.")
else:
    print("a는 b랑 다릅니다.") """
    
# or비교문
""" char = "a"
if char == "a" or char == "b":
    print("a 또는 b입니다.")
else:
    print("a 또는 b가 아닙니다.") """
    

# for 문
""" fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) """
    
""" my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num) """

""" for i in range(10):
    print(i) #0부터 9까지 """
    
""" for char in "python":
    print(char) """
    
""" fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit) # 그냥 역순
for fruit in sorted(fruits, reverse=True):
    print(fruit) # 오름 """

""" for i in range(9):
    for j in range(9):
        print(i+1,"X", j+1,"=", (i+1) * (j+1)) """
   
""" for i in range(1, 10):
    for j in range(1, 10):
        print(i,"X", j,"=", (i) * (j)) """
        
# for ~ else 문
""" rang = [5, 8, 3, 1, 6]
for i in rang:
	print("element : ", i)
else :
	print("end process") """
 
 
# 반복문 제어
""" for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass
    print(i) """
    
# while 문
""" i = 1
while i <= 5:
    print(i)
    i += 1 """
    
""" i = 0
while i <= 9:
    print(i)
    i += 1 """
    
""" char = "python"
i = 0
while i < len(char):
    print(char[i])
    i += 1 """
 
""" sum = 0   
i = 1
while i <= 10:
    sum = sum + i
    i += 1
print(sum) """

i = 1
while i <= 100:
    if i % 2 == 0:
        print("짝수:", i)
    else:
        print("홀수: ", i)
    i += 1
    
""" i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    else:
        pass
    i += 1 """