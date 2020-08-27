from discord.ext import commands
from discord.utils import get  
from discord import Embed, Colour
from random import randint

from random import choice


class random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
 

    @commands.command(aliases=['r'], brief='?roll [x]')
    async def roll(self, ctx, arg):
        try:
            float(arg)
        except:
            await ctx.send('❌ You must input an integer !')
        else:
            number = randint(1, int(arg))
            await ctx.send(f'🎲 You rolled a {number} !')


def setup(bot):
    bot.add_cog(random(bot))
