import requests
import os

# Load API key from environment variables
from dotenv import load_dotenv
load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

def get_eth_transactions(wallet_address):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}'
    print(url)
    response = requests.get(url).json()
    return response['result']

def get_erc20_transactions(wallet_address, contract_address):
    url = f'https://api.etherscan.io/api?module=account&action=tokentx&contractaddress={contract_address}&address={wallet_address}&startblock=0&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}'
    response = requests.get(url).json()
    return response['result']


print(get_eth_transactions("0x0521AF31e1106e739801441f87D599388dE4b0F9"))