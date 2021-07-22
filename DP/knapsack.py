def knapsackRec(values, weights, capacity, index):
    if capacity <= 0 or index >= len(values):
        return 0
    
    # recursive calls: take one, ingore one
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = values[index] + knapsackRec(values, weights, capacity-weights[index], index+1)
    
    profit2 = knapsackRec(values, weights, capacity, index+1)

    return max(profit1, profit2)

# top down approach
def knapsackRecDP(dp, values, weights, capacity, index):
    if capacity <= 0 or index >= len(values):
        return 0
    
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    # recursive calls: take one, ingore one
    profit1 = 0
    if weights[index] <= capacity:
        profit1 = values[index] + knapsackRecDP(dp, values, weights, capacity-weights[index], index+1)
    
    profit2 = knapsackRecDP(dp, values, weights, capacity, index+1)

    dp[index][capacity] = max(profit1, profit2)
    return dp[index][capacity]

def knapsackItr(values, weights, capacity):
    n = len(values)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    # initialize dp array
    dp = [[0 for col in range(capacity+1)] for row in range(n)]

    # when capacity is 0, then every is 0 in column 0
    for i in range(n):
        dp[i][0] = 0
    
    # if only 1 item is present
    for col in range(capacity+1):
        if weights[0] <= col:
            dp[0][col] = values[0]

    # build the table now
    for i in range(1, n):
        for col in range(1, capacity+1):
            profit1 = 0
            profit2 = 0

            # include the item if weight allows
            if weights[i] <= col:
                profit1 = values[i] + dp[i-1][col-weights[i]]
            
            # exlucde the item
            profit2 = dp[i-1][col]

            # take max of the two
            dp[i][col] = max(profit1, profit2)

    # answer will lie in the bottom right corner
    return dp[n-1][capacity]


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    # print(knapsackRec(values, weights, capacity, 0))

    dp = [[-1 for col in range(capacity+1)] for row in range(len(values))]
    # ans = dp[0][50]
    print(knapsackItr(values, weights, capacity))