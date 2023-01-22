#!/usr/bin/python3
#
# Create an Application, add the bot to your server, copy the token the '' in the last line , run this file and execute the command on your server, 
# wait up to 24 hours and you can claim your active developer badge

import nextcord
from nextcord.ext import commands
import os



bot = commands.Bot()

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' (' + str(bot.user.id) + ')')

@bot.slash_command(description="execute to claim your active developer badge")
async def badge(interaction: nextcord.Interaction):
    await interaction.send("**This is a test command to get the Active Developer Badge**\nYou will be able to claim your Active Developer Badge within 24 hours\n", ephemeral=True)

bot.run('(|\-_-_-_-_-_-_-_-_-_-_-_-_-_-/|)')