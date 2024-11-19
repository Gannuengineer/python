#strings can be in the three form 
str1 = "This is a string"
str2 = 'Ganesh'
str3 = """THIS IS A STRING"""

# escape sequence char - special->formating dena(ex - next tab , next line)
# \n - next line   \t - next tab


# basic operation 

# concatenation 
# "Hello" + "world" = "Helloworld"

str1 = "Ganesh"
len1 = len(str1)
print(len1)
 
str2 = "pathak"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))
 

# Indexing 
# Ganesh Pat
# 0123456789      index - position -> to access char

str = "Ganesh pathak"
ch = str[0]
print(ch)


#  we can not replace str character.. examples

str[6] = "S"
# output error


