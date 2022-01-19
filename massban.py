import requests
from colorama import Fore
import discord
from discord.ext import commands
import threading

TOKEN = input('Bot token: ')
print(f'For for banning write to chat: !massban')
headers = {
    "Authorization":
    f"Bot {TOKEN}"
}

client2 = commands.Bot(
        command_prefix='!',
        intents=discord.Intents.all(),
        help_command=None
)


@client2.command()
async def massban(ctx):
    await ctx.message.delete()
    servr = ctx.guild.id

    def mass_ban(i):
        sessions = requests.Session()
        sessions.put(
            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
            headers=headers
        )

    for i in range(3):
        for member in list(ctx.guild.members):
            threading.Thread(
                target=mass_ban,
                args=(member.id,)
            ).start()
client2.run(TOKEN)
