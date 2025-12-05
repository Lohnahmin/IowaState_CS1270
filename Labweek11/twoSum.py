# Lyle Osburne
# 12/04/2025
# Lab 11 - twoSum.py
# Implements several versions of the Two Sum problem.

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def twoSumDict(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return None

def twoSumLoopsAll(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result

def twoSumDictAll(nums, target):
    result = []
    pos = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in pos:
            for k in pos[need]:
                result.append([k, i])
        if x not in pos:
            pos[x] = []
        pos[x].append(i)
    return result

def main():
    nums = [2, 7, 11, 15, 7, -2]
    target = 9
    print(twoSumLoops(nums, target))
    print(twoSumDict(nums, target))
    print(twoSumLoopsAll(nums, target))
    print(twoSumDictAll(nums, target))

if __name__ == "__main__":
    main()
