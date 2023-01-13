import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
import openai

bot = commands.Bot(
  command_prefix='.',
  case_insensitive=True,
  description=None,
  intents=discord.Intents.all(),
  help_command=None
)

@bot.command()
async def Enzo(ctx,*,arg):
  query = ctx.message.content
  response = openai.Completion.create(
   api_key = str(os.getenv("API_KEY")),
   model="text-davinci-003",
   prompt=query,
   temperature=0.5,
   max_tokens=60,
   top_p=0.3,
   frequency_penalty=0.5,
   presence_penalty=0.0
)
  await ctx.channel.send(content=response['choices'][0]['text'].replace(str(query), ""))

@bot.command()
async def csv(ctx,*,arg):
  query = ctx.message.content
  response = openai.Completion.create(
  api_key = str(os.getenv("API_KEY")),
  model="text-davinci-003",
  prompt="A two-column spreadsheet of top science fiction movies and the year of release:\n\nTitle |  Year of release",
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

  await ctx.channel.send(content=response['choices'][0]['text'].replace(str(query), ""))

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name=f"Enzo Department"))
  print(f"Logged in as {bot.user.name}")

bot.run(os.environ['BOT_KEY'])
keep_alive()