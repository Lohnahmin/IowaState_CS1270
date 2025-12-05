def doubleIsolatedVowels(s):
    s = s.lower()
    vowels = ["a","e","i","o","u"]
    result = ""
    for i in range(len(s)):
        result += s[i]
        if s[i] == 0:
            continue
        if (i < len(s) - 1) and (s[i] in vowels) and (s[i - 1] not in vowels) and (s[i + 1] not in vowels):
            result += s[i]
    

    return result
#print(doubleIsolatedVowels("Hellot"))

def oddDiffCount(num):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if (num[i] - num[j]) % 2 != 0:
                count += 1
    return count
#print(oddDiffCount([1,2,3,4]))


def wordLengthFreq(s):
    s = s.lower()
    cleaned = ""
    punct = [".", ",", "!", '?']
    stop_word = ['the', 'a', 'an']
    for ch in s:
        if ch not in punct:
            cleaned += ch
    
    freq = {}
    words = cleaned.split()

    for word in words:
        length = len(word)
        if length in freq:
            freq[length] += 1
        else:
            freq[length] = 1
    return freq
#print(wordLengthFreq("hello hello hello mad mad dog dog penis what"))

def valley(s):
    count = 0
    for i in range(len(s)):
        if i == 0 or i == len(s) - 1:
            continue
        if (s[i] < s[i -1]) and (s[i] < s[i + 1]):
            count += 1
    return count
#print(valley([5,2,7,3,8,1,9]))

def neighborSum(s):
    freq = {}
    for i in range(len(s)):
        if i == 0 or i == len(s)-1:
            continue
        sum = s[i -1] + s[i + 1] 
        freq[i] = sum
    return freq
#print(neighborSum([1,2,3,4,5,6,7,8]))

def wordLengthFreq(s):
    s =  s.lower()
    cleaned = ""
    punct = [',', ',', '!', '?']
    stop_word = ['the', 'a', 'an']
    for i in s:
        if i not in punct:
            cleaned += i
    words = cleaned.split()

    freq={}

    for word in words:
        if word in stop_word:
            continue
        length = len(word)
        if length in freq:
            freq[length] += 1
        else:
            freq[length] = 1
    return freq
#print(wordLengthFreq("The big cat and the small dog ran, and ran!"))

def valueDiffMap(s):
    freq = {}
    for i in range(len(s)):
        if i == len(s)-1:
            continue
        difference = s[i] - s[i + 1]
        freq[i] = difference
    return freq
print(valueDiffMap([5,2,9]))

def neighborProducts(s):
    freq = {}
    for i in range(len(s)):
        if i == 0 or i == len(s)-1:
            continue
        product = s[i - 1] * s[i + 1]
        freq[i] = product
    return freq
print(neighborProducts([2, 5, 3, 6]))

def a(num):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if (num[i] * num[j]) % 2 == 0:
                count += 1
    return count

def b(s):
    result = ""
    for i in range(len(s)):
        result += s[i]
        if i < len(s)- 2 and ((s[i] == s[i + 1]) or (s[i] == s[i + 2])):
            result += s[i]
    return result
print(b("hello"))

def c(s):
    s = s.lower()
    cleaned = ""
    punct = ['.', ',', '!', '?']
    word_stop = ['in', 'on', 'at']
    for i in s:
        if i not in punct:
            cleaned += i
    freq = {}
    words = cleaned.split()
    for word in words:
        if word in word_stop:
            continue
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(c("in the boat on a sunny day day"))  


def e(add, isMember):
    base = 10
    addon = 5
    discount = (add // 4) * 3
    if isMember == True:
        loyalty = 2
    else:
        loyalty = 0
    tax = 0.06
    pre_tax = base + (addon * add) - loyalty - discount
    taxed =  pre_tax * tax
    total = taxed + pre_tax
    return total

def a(num):
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if (num[i] + num[j]) % 4 == 0 and (num[i] + num[j]) % 8 != 0:
                count += 1
    return count
print(a([2,2,4,4]))

def b(s):
    result = ""
    for i in range(len(s)):
        result += s[i]
        if i == 0 or i >= len(s)-2:
            continue
        if s[i] == s[i - 1] or s[i] == s[i + 2]:
            result += s[i]
    return result
print(b("helelo"))