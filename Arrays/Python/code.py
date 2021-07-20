import math 

# create a function to find maximum size subarray of size k
def maxSubarray(arr, k):
    ans = 0
    start = 0
    slidingSum = 0

    for end in range(len(arr)):
        slidingSum += arr[end]
        if end >= k-1:
            ans = max(ans, slidingSum)
            slidingSum -= arr[start]
            start += 1

    return ans



def minSubArrSumS(arr, s):
    minLength = math.inf
    start = 0
    slidingSum = 0

    for end in range(len(arr)):
        slidingSum += arr[end]

        # we are going to shrink the window as small as possible when we have found the answer
        while slidingSum >= s:
            minLength = min(minLength, end - start + 1)
            slidingSum -= arr[start]
            start += 1
    if minLength == math.inf:
        return 0
    return minLength
