from brownie import accounts,config,TokenERC20
import math

initial_supply=math.pow(10,18)
token_name="Token"
token_symbol="TKN"
def main():
    account=accounts.add(config["wallets"]["from_key"])
    erc20=TokenERC20.deploy(initial_supply,token_name,token_symbol,{"from": account},publish_source=True) 