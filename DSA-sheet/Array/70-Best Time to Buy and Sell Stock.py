prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')  # Start with the largest possible value
max_profit = 0  # No profit initially
n = len(prices)
for i in range(0, n):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit, prices[i] - min_price)

print(max_profit)
