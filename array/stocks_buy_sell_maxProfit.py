# Approach 1
# Naive approach: A simple approach is to try buying the stocks and selling them on every single day when profitable and keep updating the maximum profit so far.
def maxProfit(price, start, end):
    # if stock is not sellable
    if end <= start:
        return 0

    profit = 0

    for i in range(start, end):
        for j in range(i+1, end+1):

            if price[j] > price[i]:
                currProf = price[j] - price[i] + maxProfit(price, start, i-1) + maxProfit(price, j+1, end)

                profit = max(profit, currProf)

    return profit



price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)
print(maxProfit(price, 0, n-1))

# Approach 2
# Efficient approach: If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. 
# Find the local minima and store it as starting index. If not exists, return.
# Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
# Update the solution (Increment count of buy sell pairs)
# Repeat the above steps if end is not reached.

def stockBuySell(price, n):
    # Prices must be given for at least two days
    if n == 1:
        return

    # Traverse through the price array
    i = 0
    while i < n-1:

        # find the local minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while (i < n-1) and (price[i+1] < price[i]):
            i += 1
        
        # Reached the end, no solution
        if i == (n-1):
            break

        buy = i
        i += 1

        # find the local maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while (i < n) and (price[i] > price[i-1]):
            i += 1

        sell = i - 1

        print("Buy on day: ", buy, "\t", "Sell on day: ", sell)

price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)
print(stockBuySell(price, n))