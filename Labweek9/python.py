def evenSumCount(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (numbers[i] + numbers[j]) % 2 == 0:
                count += 1
    return count
#print(evenSumCount([2, 2, 2]))

def doubleNeighbors(s):
    s = s.lower()
    result = ""
    for i in range(len(s)):
        result += s[i]
        if i < len(s) - 1 and s[i] == s[i + 1]:
            result += s[i]
    return result
    
#print(doubleNeighbors("Hello"))

def frequentWords(s):
    s = s.lower()
    cleaned = ""
    for ch in s:
        if ch not in [".","!",",","?"]:
            cleaned += ch
    freq = {}
    words = cleaned.split()
    for s in words:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
    return freq
#print(frequentWords("The cat and the dog."))


def calculateTotal(std, prem, isMember):
    base_plan = 12.99
    standard = 4
    premium = 7
    promotion = (std // 3) * 2
    tax = 0.07

    subtotal = base_plan + (standard * std) + (prem * premium) - promotion 
    if isMember == True:
        subtotal -= 5
    total_tax = subtotal * tax
    total = subtotal + total_tax
    return total
print(calculateTotal(4,3,False))


