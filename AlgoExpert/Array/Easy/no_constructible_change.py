def non_constructible_change(coins):

    current_change = 0

    for coin in coins:
        if coin > current_change + 1:
            return current_change + 1
        
        current_change += coin
    
    return current_change + 1

print(non_constructible_change([1,2,5]))
