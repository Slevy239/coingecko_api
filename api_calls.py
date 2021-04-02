from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

btc = 'bitcoin'
eth = 'ethereum'
uni = 'uniswap'
link = 'chainlink'
coins = [btc, eth, uni, link]

# While loop iterating through the coin list
i = 0
while i < len(coins):
    # prints all values in list
    print(cg.get_price(ids=coins[i], vs_currencies='usd'))
    i += 1


# allows for user input
while input("Would you like to continue?\n") == 'yes':
    new = input('Enter a value\n')
    # check if values exists in the list
    if new in coins:
        print('choose a new value')
    # appends list and prints updated list
    else:
        coins.append(new)
        k = 0
        while k < len(coins):
            print(cg.get_price(ids=coins[k], vs_currencies='usd'))
            k += 1
