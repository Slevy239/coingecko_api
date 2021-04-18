import json
import requests
import config

# Potential Sushiswap farm rewards

url = 'https://raw.githubusercontent.com/sushiswap/sushi-vesting/master/amounts-10959148-12171394.json'
merkle_1 = 'https://raw.githubusercontent.com/sushiswap/sushi-vesting/master/merkle/week-01/merkle-10959148-11003985.json'
resp2 = requests.get(merkle_1)
data2 = json.loads(resp2.text)
resp = requests.get(url)
data = json.loads(resp.text)

mine = config.address
josh = config.sutker
coop = config.coop
address = []

if mine in data:
    address.append(mine)
    address.append(josh)
    address.append(coop)
# if mine in data2:
    # address.append(mine)
    # address.append(mine)


print(address, 'addresses?')
