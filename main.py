import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration using environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TARGET_CHANNEL_ID = int(os.getenv('TARGET_CHANNEL_ID'))
API_GATEWAY_URL = os.getenv('API_GATEWAY_URL')

# Initialize the bot with necessary permissions to listen for messages
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} est connecté à Discord et prêt à écouter!')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message comes from the target channel
    if message.channel.id == TARGET_CHANNEL_ID:
        # Check if the message matches a specific text, e.g., "test123"
        if message.content == "test123":
            # Send a POST request to the API Gateway
            try:
                response = requests.post(API_GATEWAY_URL, json={'content': message.content})
                if response.status_code == 200:
                    # If the API request is successful, send a confirmation message in the Discord channel
                    await message.channel.send("Message envoyé avec succès à l'API Gateway.")
                else:
                    await message.channel.send(f"Erreur lors de l'envoi: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                await message.channel.send(f"Erreur de requête : {e}")

# Run the bot
bot.run(DISCORD_TOKEN)
