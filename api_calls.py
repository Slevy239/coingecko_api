from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

btc = 'bitcoin'
eth = 'ethereum'
uni = 'uniswap'
link = 'chainlink'
coins = [btc, eth, uni, link]


def print_list():
    # While loop iterating through the coin list
    i = 0
    while i < len(coins):
        # prints all values in list
        print(cg.get_price(ids=coins[i], vs_currencies='usd'))
        i += 1
    user_input()


def user_input():
    # allows for user input
    # while input("Would you like to continue?\n") == 'yes':
    new = input('Enter a value\n')

    # check if values exists in the list
    if new in coins:
        print('Already exists in the list')
        user_input()
    # appends list and prints updated list
    else:
        coins.append(new)
        k = 0
        while k < len(coins):
            print(cg.get_price(ids=coins[k], vs_currencies='usd'))
            k += 1
    user_input()

print_list()
