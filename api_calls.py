from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

btc = 'bitcoin'
eth = 'ethereum'
uni = 'uniswap'
link = 'chainlink'
coins = [btc, eth, uni, link]

print(cg.get_price(ids=coins[1], vs_currencies='usd'))

# i = 0
# while i < len(coins):
#     print(cg.get_price(ids=coins[i], vs_currencies='usd'))
#     i += 1
