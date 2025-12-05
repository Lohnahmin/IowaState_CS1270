#Lyle Osburne
#10-30-2925
#Lab 7
# a function that finds the mean and median of a randomly generated list

import random

def generateInput():
    list_length = random.randint(200, 500)

    rand_list = []
    for i in range(list_length):
        rand_list.append(random.randint(1, 2000))

    return rand_list

def findMean(random_list):
# A mean is when you add up all values and then divide by number of values
#https://www.dictionary.com/e/average-vs-mean-vs-median-vs-mode/
    total = 0
    for i in random_list:
        total += i
    list_mean = total / len(random_list)
    return list_mean

def findMedian(random_list):
#A median is a set of numbers in increasing value and you find the middle one
#If the set of numbers is even the median is the mean of the middle two values
#https://www.dictionary.com/e/average-vs-mean-vs-median-vs-mode/
    random_list.sort()
    length = len(random_list)

    if length % 2 == 0:
        mid = random_list[length // 2 - 1]
        mid2 = random_list[length // 2]
        list_median = (mid + mid2) / 2
    else:
        list_median = random_list[length // 2]
    return list_median
def main():
    random_list = generateInput()
    mean = findMean(random_list)
    median = findMedian(random_list)
    print(f"Mean: {mean} Median: {median}")

if __name__ == "__main__":
    main()
