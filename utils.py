import os
from dotenv import load_dotenv


load_dotenv()
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')


def calculate_totals(transactions, wallet_address):
    total_bought = 0
    total_spent = 0
    total_sold = 0
    total_received = 0
    
    for tx in transactions:
        token_value = int(tx['value']) / (10 ** int(tx['tokenDecimal']))  # Convert value based on token decimals
        gas_cost = int(tx['gas']) * int(tx['gasPrice']) / (10 ** 18)  # Gas cost in Ether

        if tx['to'].lower() == wallet_address.lower():  # Buying tokens (wallet receives tokens)
            total_bought += token_value
            total_spent += gas_cost  # Add gas cost to the total amount spent
        elif tx['from'].lower() == wallet_address.lower():  # Selling tokens (wallet sends tokens)
            total_sold += token_value
            total_received += gas_cost  # Add gas cost to the total amount received
    
    return total_bought, total_spent, total_sold, total_received

