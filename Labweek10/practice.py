"""def count_vowels(s):
    s = s.lower()
    vowel = ["a",'e','i','o','u']
    i = 0
    count = 0
    while i < len(s):
        if s[i] in vowel:
            count += 1
        i += 1
    return count
print(count_vowels("HelloO"))"""

"""s = "Hel5lo6234"
clean = ""
i = 0
count = 0
while i < len(s):
    if s[i] not in "1234567890":
        clean += s[i]
    i += 1
print(clean)
"""

"""s = "dickbuttkiss#69"
i = 0
clean = ""

while s[i] != "#":
    clean += s[i]
    i += 1
print(clean)"""

"""s = 'boak'
i = 0
identical = False
while not identical and i < len(s) -1:
    if s[i] == s[i+1]:
        identical = True
    i += 1
if identical == True:
    print("yes")
else:
    print("no")
        """

"""nums = range(1, 15)

i = 0
num = []

while i < len(nums):
    if nums[i] > 10:
        num.append(nums[i])
    i += 1
print(num)"""



"""s = "Dick Butt ass FUCKNUGGETSa aaaaaaaa target target targett"
s = s.lower()
i = 0
word = s.split()
count = 0

while i < len(word):
    if word[i] in "target":
        count += 1
    i += 1
print(count)"""

"""def negatives(nums):
    positive = []
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            positive.append(nums[i])
        i += 1
    return positive
print(negatives([1,2,-3,-4,5,-6]))"""

"""s = input("blah")
count = 0
while i < len(s) and s != "quit":
    if "yes" in s:
        count += 1
    s = input("blah blah")
print(count)"""

"""def compress(s):
    i = 0
    result = ""

    while i < len(s):
        ch = s[i]
        i += 1
        count = 1
        
        while i < len(s) and s[i] == ch:
            count += 1
            i += 1

        result += ch + str(count)

    return result

print(compress("ddddiiiiiccccckkkk"))
"""

"""def increase(s):
    result = False
    i = 0
    while i < len(s) - 2:
        if s[i] < s[i+1] and s[i+1]< s[i+2]:
            result = True
        i += 1
    return result
print(increase([1,2,2]))
        """

"""s = "as324 2ca t34da sd cccc csA32 42S55 at34c at2   DAD34223   4da@!@#sdas"
ss = s.split()
b = -1    
count = 0
new = ""
what = False
i = 0
j = 0
while i < len(ss):
    word = ss[i]
    j = 0
    while j < len(word):
        if word[j] == "a":
            count += 1
        j += 1
    i += 1
print(count)"""

s = "as3324  2ca t34da sd cccccccccccccc c!sA32 42S55 at34c at2   DAD34223   4da@!@#sdas"
ss = s.split()
b = -1    
count = 0
new = ""
what = False
i = 0
j = 0

new = ""
best_count = 0
char = ""
for i in s:
    count = 0
    for j in s:
        if j == i:
            count += 1
    if count > best_count:
        best_count = count
        char = i
print(char)

sss = "python rocks"
print(sss[1] * sss.index("n"))


    


