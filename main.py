import os
from dotenv import load_dotenv
import discord
from keep_alive import keep_alive

static void UpdatePresence()
{
    DiscordRichPresence discordPresence;
    memset(&discordPresence, 0, sizeof(discordPresence));
    discordPresence.state = "Playing Solo";
    discordPresence.details = "Competitive";
    discordPresence.startTimestamp = 1507665886;
    discordPresence.endTimestamp = 1507665886;
    discordPresence.largeImageKey = "tuvaallerenenfertoi";
    discordPresence.largeImageText = "Numbani";
    discordPresence.smallImageText = "Rogue - Level 100";
    discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657";
    discordPresence.partySize = 1;
    discordPresence.partyMax = 5;
    discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= ";
    Discord_UpdatePresence(&discordPresence);
}

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
