my_list = [0,1,2,3,4,5,6,7,8,9]
result1 = my_list[1:4]
print(result1)

my_tuple = (0,1,2,3,4,5,6,7,8,9)
result2 = my_tuple[:]
print(result2)

my_str = "0123456789"
result3 = my_str[::2]
print(result3)

my_str = "0123456789"
result4 = my_str[::-1]
print(result4)

my_tuple = (0,1,2,3,4,5,6,7,8,9)
result5 = my_tuple[3:1:-1]
print(result5)

my_list = [0,1,2,3,4,5,6,7,8,9]
result6 = my_list[::-2]
print(result6)