# type conversion
a = 2
b = 4.25
print(a + b)  # 2.0 + 4.25 >= 6.25

a = "2"
b = 4.25
print(a + b)  # error bcz "2" is string 
# for this we will use type casting

c = int(a)  # or a = int("2")
print(c + b )

a = 3.14
a = str(a)

print(type(a))

