def a1(num):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if (abs(num[i]) - num[j]) % 2 != 0:
                count += 1
    return count
#print(a1([1,2,3,4]))

def a3(num):
    count = 0

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] % 3 == 0:
                count += 1
    return count
def a5(num, low, high):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            total = num[i] + num[j]
            if low <= total <= high:
                count += 1

    return count
#print(a5([1,2,3,4,5], 2, 7))

def b1(s):
    result =""
    for i in range(len(s)):
        result += s[i]
        if i == 0:
            continue
        if s[i] == s[i - 1]:
            result += s[i]

def b2(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    result = ""
    s = s.lower()
    for i in range(len(s)):
        result += s[i]
        if i == len(s)-1:
            continue
        if s[i] in vowel and s[i + 1] in vowel:
            result += s[i] * 2
    return result
print(b2("heello"))

def b5(s):
    result = ""
    for i in range(len(s)):
        result += s[i]
        if i != 0 and  i < len(s)-1 and s[i-1] == s[i + 1]:
            result += s[i+1]
    return result
print(b5("lele"))