# Example Input
prices = [7, 1, 5, 3, 6, 4]

def max_profit(prices):

    # Smallest price seen so far (potential buying price)
    min_price = float('inf')

    # Maximum profit found so far
    max_profit_so_far = 0

    # To store actual buy and sell prices
    buy_price = 0
    sell_price = 0

    for price in prices:

        # Update minimum price if a cheaper stock is found
        if price < min_price:
            min_price = price

        # Profit if we sell today
        current_profit = price - min_price

        # Update maximum profit if current profit is better
        if current_profit > max_profit_so_far:
            max_profit_so_far = current_profit
            buy_price = min_price
            sell_price = price

    print("Buy at :", buy_price)
    print("Sell at:", sell_price)

    return max_profit_so_far


print("Maximum Profit =", max_profit(prices))