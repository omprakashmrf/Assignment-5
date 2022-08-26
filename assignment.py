x = 12345
y = int(str(x)[:-1])
print(y)
z = int(str(x)[-1])
print(z)
a = 5 
b = 6
a = a + b
b = a - b
a = a - b
print(a, b)

xx = int(input("enter the base number "))
yy = int(input("enter the power number "))

result = xx**yy
print(result)

user_input = int(input("enter the input "))
result2 = int(str(user_input)[:1])
print(result2)

user_input = int(input("enter the input "))
if len(str(user_input))==3:
    result3 = int(str(user_input)[1:-1])
    print(result3)
else:
    print("entered number length are not three")

user_input = int(input("enter the input "))
if len(str(user_input))==3:
    result4 = int(str(user_input)[-1])
    print(result4)
else:
    print("entered number length are not three")
    
list1 = [1,3,5,6,8]
if 3 in list1:
     print("three prasent in list1")
else:
    print("not prasent")

usr = int(input("enter number "))
list1 = [1,3,5,6,8]
if usr not in list1:
    print("number not prasent in list1")
    list1.append(usr)
    print("now prasent")
else:
    print("number already prasent")    
    
a = 100
b = 100

result = a is b
print(result)    
    


