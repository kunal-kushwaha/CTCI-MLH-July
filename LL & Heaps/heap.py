from heapq import *

def klargest(nums, k):
    minHeap = []

    # put first k numbers in the heap
    for num in range(k):
        heappush(minHeap, nums[num])

    # go through the remaing numbers
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9,10, 1, 2, 3]
    print(klargest(nums, 3))
