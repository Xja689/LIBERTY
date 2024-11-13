import os
from dotenv import load_dotenv
import discord
from keep_alive import keep_alive



client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith("769204"):
        membre = message.author
        server = client.get_guild (1289529811751927881)
        role = server.get_role (1289549610892791909)
        await membre.add_roles(role)


load_dotenv()
TOKEN=os.getenv('DICORD_TOKEN')

keep_alive()
client.run(token=TOKEN)
