""" my_set = set({5, 8, 3, 7, 1, "h"})
print(my_set)
print(*my_set)

set_tmp = set("hello")
print(set_tmp) """

""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"} """

#집합
# print(my_set | set_item)

# print(my_set.union(set_item))

# print(my_set - set_item)

# print(my_set.difference(set_item))

# print(my_set & set_item)

# print(my_set.intersection(set_item))


#추가
""" print(my_set)
my_set.add(9)
print(my_set) """

""" print(my_set)
my_set.update([5, 9, 7, 4])
print(my_set) """

""" print(my_set)
my_set.clear()
print(my_set) """

""" print(my_set)
my_set.remove(5) # remove는 없는거 삭제하면 오류남
print(my_set) """

""" print(my_set)
my_set.discard(2)
print(my_set) """

""" print(my_set)
my_set.difference_update(set_item)
print(my_set) """


# 타입변환
""" my_int = 10
my_str = str(my_int) """

""" my_int = 10
print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)
# print(my_str + 10) 오류남 변수 안맞아서

print(my_str + "hello") """


""" my_str = '10' 
my_int = int(my_str)

print(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int("ten")
print(my_int2) #안됨 """


#연산
a = 10
b = 3

# print(a + b)    
# print(a - b)    
# print(a * b)    
# print(a / b)    
# print(a % b)    
# print(a // b)   
# print(a ** b)

""" a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a)

a /= 2
print(a)

a **= 3
print(a) # 연산자 숫자값을 저장해가며 숫자값을 만든다 """


# 비교관계 연산자
""" a = 10
b = 4 """

# print(a > b)    
# print(a < b)    
# print(a >= b)   
# print(a <= b)   
# print(a == b)   # 같냐?
# print(a != b)   # 다르냐?

#논리연산자
""" a = 1
b = 0

print(a and b)
print(a or b)
print(not a)
print(not b)

x = True
y = False

print(x and y)  
print(x or y)   
print(not x)    
print(not y)  """


# 멤버 연산자
my_list = [9, 4, 3, 7, 8, 'hi']
print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_dic)

