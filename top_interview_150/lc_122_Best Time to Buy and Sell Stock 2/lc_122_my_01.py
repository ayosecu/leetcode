def main(prices):
    size_prices = len(prices)

    if size_prices < 2:
        return 0
    
    i = 0
    profit = 0
    for i in range(1, size_prices):
        if prices[i] - prices[i-1] > 0:
            profit += prices[i] - prices[i-1]
    print(profit)
    return

if (__name__ == "__main__"):
    tc = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [1, 2],
            [2, 4, 1]
         ]
    
    for t in tc:
        main(t)
    
