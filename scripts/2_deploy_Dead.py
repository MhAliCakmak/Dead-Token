from brownie import accounts,config,DeadToken

import math

initial_supply=math.pow(10,18)

def main():
    account=accounts.add(config["wallets"]["from_key"],)
    erc20=DeadToken.deploy(initial_supply,{"from": account},publish_source=True) 