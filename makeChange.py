# Given the input 387 return a dictionary with the values
# {'dollars': 3, 'quarters': 3, 'dimes': 1, 'nickles': 0, 'pennies': 2}

def change(cents):
    amount = {}
    coins = [(100, 'dollars' ), (25, 'quarters'), (10, 'dimes'), (5, 'nickles'), (1, 'pennies')]
    for coin_value, coin_name in coins:
        if cents >= coin_value:
            number_coin, cents = divmod(cents, coin_value)
            amount[coin_name] = number_coin
    return amount
    
print change(387)