def main(prices):
    size_prices = len(prices)
    if size_prices < 2:
        return 0
    
    i = 0
    min_idx = 0
    max_idx = 0
    diff = 0
    while i < size_prices:
        if prices[i] < prices[min_idx]:
            min_idx = i
            if max_idx < min_idx:
                max_idx = min_idx
        
        if prices[i] > prices[max_idx]:
            max_idx = i
            if prices[max_idx] - prices[min_idx] > diff:
                diff = prices[max_idx] - prices[min_idx]
        i += 1

    return diff

if (__name__ == "__main__"):
    tc = [
            [7, 1, 5, 3, 6, 4],
            [7, 6, 4, 3, 1],
            [1, 2],
            [2, 4, 1],
            [1],
            [3,2,6,5,0,3]
         ]
    
    for t in tc:
        print(main(t))
