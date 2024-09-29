import discord
import os
from dotenv import load_dotenv
from etherscanio_utils import get_eth_transactions, get_erc20_transactions
from utils import get_token_price_at_time, calculate_profit_and_roi
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
ETHERSCAN_API_KEY = os.getenv('ETHERSCAN_API_KEY')

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ethprice'):
        wallet_address = 'your_wallet_address_here'  # Change this to user-provided wallet address if necessary
        transactions = get_eth_transactions(wallet_address)
        current_price = get_token_price_at_time('ethereum', datetime.now())

        profit, roi = calculate_profit_and_roi(transactions, current_price, wallet_address, get_token_price_at_time)
        await message.channel.send(f'Profit: ${profit}, ROI: {roi}%')

client.run(DISCORD_TOKEN)
