from pycoingecko import CoinGeckoAPI
import etherscan
import config

cg = CoinGeckoAPI()

btc = 'bitcoin'
uni = 'uniswap'
link = 'chainlink'
xtk = 'xtoken'
aave = 'aave'
coins = [btc, uni, link, xtk, aave]

es = etherscan.Client(
    api_key=config.api_key,
    cache_expire_after=5,
)
wallet = es.get_eth_balance(config.address)
wei = wallet * 10 ** -18
gas = es.get_gas_price()
eth_price = es.get_eth_price()

eth_usd = []
for i in eth_price:
    eth_usd.append(eth_price[i])
print("Ethereum: ", eth_usd[2])
print(gas * 10 ** -9, ' GWEI')
print(round(wei, 2), ' ETH')
print(round(wei * eth_usd[2], 2), " USD")


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
    new = input('Enter a value\n').strip()

    # check if values exists in the list
    if new in coins:
        print('Already exists in the list\n')
        user_input()
    # appends and prints updated list
    else:
        coins.append(new)
        k = 0
        while k < len(coins):
            print(cg.get_price(ids=coins[k], vs_currencies='usd'))
            k += 1
    user_input()


print_list()

