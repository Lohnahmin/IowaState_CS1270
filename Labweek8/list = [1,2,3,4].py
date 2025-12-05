list1 = [1,2,3,4]


min_num = list1[0]
print(min_num)
for i in list1:
    if i < min_num:
        min_num = i
print(min_num)