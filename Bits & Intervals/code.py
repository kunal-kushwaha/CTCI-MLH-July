# arr = [2, 3, 2, 1, 4, 4, 1]

# ans = 0

# for num in arr:
#     ans ^= num

# print(ans)

# import math

# n = 23456789876543234567
# b = 8
# digits = int(math.log(n, b)) + 1
# print(digits)

# find the missing number from range 0 to n
li = [1, 4, 0, 3] # ans should be 2

def findMissingNumber(li):
    i = 0
    while i < len(li):
        j = li[i]
        if li[i] < len(li) and li[i] != li[j]:
            # swap
            li[i], li[j] = li[j], li[i]
        else:
            i += 1

    # find the missing number from its index
    for i in range(len(li)):
        if li[i] != i:
            return i
    
    return n

print(findMissingNumber(li))