import discord
import os
from dotenv import load_dotenv
from etherscanio_utils import get_eth_transactions, get_erc20_transactions, get_erc20_token_transfers
from utils import calculate_totals
from datetime import datetime

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')


transactions = get_erc20_token_transfers("0x0521AF31e1106e739801441f87D599388dE4b0F9", "triangle")
# Calculate totals
total_bought, total_spent, total_sold, total_received = calculate_totals(transactions, "0x0521AF31e1106e739801441f87D599388dE4b0F9")

# Calculate profit
profit = total_received - total_spent

# Calculate ROI
roi = (profit / total_spent) * 100 if total_spent != 0 else 0

# Output results
print(f"Total Bought: {total_bought}")
print(f"Total Spent (ETH in gas fees): {total_spent}")
print(f"Total Sold: {total_sold}")
print(f"Total Received (ETH in gas fees): {total_received}")
print(f"Profit: {profit}")
print(f"ROI: {roi:.2f}%")