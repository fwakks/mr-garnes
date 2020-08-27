from discord import Embed
from discord.ext import commands

from requests import get 
from datetime import datetime
from datetime import timedelta

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='?weather [city]')
    async def weather(self, ctx,  *, city):
        data = get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID=0d5e7ba8991935f927322ccbb1a596b0").json()
        cleared_data = {
            'City': data['name'],
            'Time':(datetime.utcfromtimestamp(data['dt']) + timedelta(hours=-4)).strftime('%H:%M:%S'),
            'Weather': f"{data['weather'][0]['main']} - {data['weather'][0]['description']}",
            'Temperature': f"{data['main']['temp']}°F",
            'Feels like': f"{data['main']['feels_like']}°F",
            'Min temperature': f"{data['main']['temp_min']}°F",
            'Max temperature': f"{data['main']['temp_max']}°F",
            'Humidity': f"{data['main']['humidity']}%",
            'Pressure': f"{data['main']['pressure']}Pa",
            'Clouds': f"{data['clouds']['all']}%",
            'Wind': f"{data['wind']['speed']} mph",
            'Sunset': (datetime.utcfromtimestamp(data['sys']['sunset']) + timedelta(hours=-4)).strftime('%H:%M:%S'),
            'Sunrise': (datetime.utcfromtimestamp(data['sys']['sunrise']) + timedelta(hours=-4)).strftime('%H:%M:%S'),
        }
        embed = Embed(title=f":white_sun_small_cloud: Weather in {cleared_data['City']}", color=0x3498db)
        for key, value in cleared_data.items():
            embed.add_field(name=key, value=value)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Weather(bot))
