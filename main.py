import discord
import os 
import requests
import random
import json
import praw
import asyncio
import subprocess
from flask import Flask
from threading import Thread
from replit import db
from discord.ext import commands
from discord.flags import Intents


#Flask server setup
app = Flask('Walt.jr Web app')

@app.route('/')
def home():
    return "Hello. I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8000)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()

# Define your bot's prefix
prefix = "!"

# Initialize the bot
bot = commands.Bot(command_prefix=prefix, intents=Intents.all())

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.invites = True


def get_weather(location):
    # OpenWeatherMap API key
    API_KEY = "6ec986e3de0dce6f6cc981d3fd8b249b"
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    # Send a GET request to the API
    response = requests.get(url)
    # If the request was successful, return the weather data
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Dictionary to store monitored subreddits
monitored_subreddits = {}

#define meme command
def fetch_random_meme(subreddit_name):
  subreddit = reddit.subreddit(subreddit_name)
  memes = []
  # Fetch memes from the specified subreddit
  for submission in subreddit.hot(limit=100):
      # Consider only posts with images
      if submission.url.endswith(('jpg', 'jpeg', 'png')):
          memes.append(submission.url)

  # Check if memes list is empty
  if not memes:
      return "No memes found in this subreddit."

  # Return a random meme URL
  return random.choice(memes)

# Initialize the Reddit API wrapper
reddit = praw.Reddit(client_id='ta6z73U-tDYVWCCeUlTpkQ',
                     client_secret='0RoFKzvRIkvnVAFHWRAK-zPdiajYvA',
                     user_agent='discord:RedditBot:v1.0 (by /u/ArunSteve)')

#Dfine the Welcome Channel ID
WELCOME_CHANNEL_ID = 1224443049984397352

# Define the rules channel ID
RULES_CHANNEL_ID = 1224443099510738994

# Define the Tv-Show Channel ID
TV_SHOWS_CHANNEL_ID = 1224443444508889200

# Define the Movie Channel ID
MOVIES_CHANNEL_ID = 1224443490209894610

#Define the Bot Command ID
BOT_COMMANDS_ID = 1227348329717829673

# define the funfact.
fun_facts = [
    "The first computer virus was created in 1983 and was called the 'Elk Cloner.' It infected Apple II systems through floppy disks.",
    "The first programmer in history was Ada Lovelace, an English mathematician. She wrote the first algorithm intended to be processed by a machine, making her the world's first computer programmer.",
    "The term 'bug' in computer science originated from an incident in 1947 when a moth got trapped in a relay of the Harvard Mark II computer, causing a malfunction. Engineers then 'debugged' the computer to remove the moth, coining the term.",
    "The world's first website went live on August 6, 1991. It was created by Tim Berners-Lee and provided information about the World Wide Web project.",
    "The first computer mouse was invented in 1964 by Douglas Engelbart. It was made of wood and had two wheels that could roll in any direction.",
    "The average computer has around 2 billion transistors. Transistors are the building blocks of modern computer processors and memory chips.",
    "The QWERTY keyboard layout, which is commonly used in English-speaking countries, was designed in the 1860s by Christopher Sholes. It was originally created to prevent jamming in typewriters.",
    "The first electronic digital computer, ENIAC, weighed more than 27 tons and occupied a space of about 1,800 square feet. It was completed in 1945.",
    "The concept of a 'byte' was coined by Dr. Werner Buchholz in 1956 while working at IBM. It represents a sequence of bits (usually 8) used to encode a single character of text in a computer.",
    "The shortest-ever program written was just one line long. It was written in the programming language APL and printed 'Hello, World!' when executed."
    "The first computer program was written by Ada Lovelace for Charles Babbage's Analytical Engine. It was an algorithm to calculate Bernoulli numbers, making her the world's first computer programmer.",
    "The concept of a 'bit' (short for binary digit) was introduced by Claude Shannon in his 1937 master's thesis. He laid the groundwork for digital circuit design theory, which is essential for modern computer engineering.",
    "The first computer bug was not a moth but a real insect. In 1947, engineers found a dead cockroach stuck in a relay of the Harvard Mark II computer, causing a malfunction. This incident inspired the term 'bug' in computer science.",
    "The term 'software engineering' was first used in 1968 during NATO's Software Engineering Conference. It aimed to address the challenges of developing large-scale software systems.",
    "The concept of cloud computing dates back to the 1960s when J.C.R. Licklider envisioned an 'intergalactic computer network' that would allow everyone to access data and programs from anywhere.",
    "The Apollo 11 guidance computer, which landed the first humans on the moon, had less computing power than a modern smartphone. It operated at 1.024 MHz and had just 64 KB of memory.",
    "The World Wide Web was invented by Tim Berners-Lee in 1989 while working at CERN. He proposed a decentralized system of information sharing using hypertext, leading to the creation of the first web browser and web server.",
    "The famous Konami Code (up, up, down, down, left, right, left, right, B, A) originated in 1986 in the video game 'Gradius' by Konami. It has since become a cultural phenomenon and is often used as an Easter egg in various software and websites.",
    "The concept of virtual reality (VR) was first introduced in the 1960s by Ivan Sutherland, who created the first VR head-mounted display called the 'Sword of Damocles.' It laid the foundation for modern VR technology.",
    "The first known computer virus to spread over a network was the Morris Worm, created by Robert Tappan Morris in 1988. It infected thousands of Unix machines and caused significant disruption to the early internet."
]

# Declare the lists
frustrating_words = [
    "I'll never be as successful as others",
    "I keep failing at everything",
    "I'm not good enough to achieve my goals",
    "I always mess things up",
    "I feel like giving up",
]

uplifting_words = [
    "Believe in yourself, you've got this!",
    "Every setback is an opportunity to learn and grow.",
    "Keep pushing forward, you're stronger than you think!",
    "You're capable of achieving great things, don't give up!",
    "Remember, progress is not always linear. Keep going!"
]
tv_shows = [ "Breaking Bad", "Better Call Saul", "How to sell drugs online", 
            "Avatar The Last Airbender", "Dark", "1899", 
            "Bojack Horseman", "The Walking Dead", "Loki", 
            "The Boys", "Game of Thrones", "Sex Education",
            "Stranger Things", "The Bear", "The Crown", 
            "Friends", "Black Mirror", "The Office", 
            "Narcos", "Sherlock", "The Mandalorian",
            "Suits", "Vikings", "Family Guy", 
            "The Simpsons", "The Big Bang Theory", "Rick and Morty", ]

# Define the bot's prefix
movies_list = [
  "The Silence of the Lambs", 
  "Saving Private Ryan", "Gladiator",
  "The Departed",   "The Prestige",
  "Interstellar", "Forrest Gump",
  "The Green Mile", "Pulp Fiction",
  "The Shawshank Redemption","Schindler's List",
  "The Matrix","Fight Club", "The Dark Knight Trilogy",
  "Inception", "The Lord of the Rings",
  "The Godfather Trilogy", "The Social Network",
  "Avatar","A Beautiful Mind",
  "The Bourne Identity", "Titanic",
  "The Pursuit of Happyness",
  "The Notebook",
  "Catch Me If You Can", "The Hangover Trilogy",
  "The Great Gatsby", "The Wolf of Wall Street",
  "Shutter Island", "Weathering with You anime"
  "Inglourious Basterds", "The Green mile",
  "Whiplash","La La Land" ,"You Name Anime",
]

# Define function to update encouragements
def update_encouragements(encouraging_message):
    global uplifting_words
    uplifting_words.append(encouraging_message)

# Define function to delete encouragements
def delete_encouragement(index):
    global uplifting_words
    if index >= 0 and index < len(uplifting_words):
        del uplifting_words[index]

# Define function to get a quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    json_data = response.json()
    quote = json_data[0]['q'] + " _" + json_data[0]['a']
    return quote

@bot.event 
async def on_ready():
  print(" We have logged in as {0.user}".format(bot))

@bot.event
async def on_member_join(member):
    welcome_channel = member.guild.get_channel(WELCOME_CHANNEL_ID)  # Replace YOUR_WELCOME_CHANNEL_ID with the actual ID of your welcome channel
    if welcome_channel:
        await welcome_channel.send(f'Welcome {member.mention}! :wave: :tada:')
# Send direct message to the new member if DMs are enabled
    if member.dm_channel is None:
        await member.create_dm()  # Create a DM channel if one doesn't exist
    try:
        await member.dm_channel.send(f'Welcome to the server, {member.name}! We hope you enjoy your time here.')
    except:
        pass  # Ignore any errors while sending the DM

@bot.event
async def on_member_remove(member):
    # Send goodbye message in the welcome channel
    welcome_channel = member.guild.get_channel(WELCOME_CHANNEL_ID)
    if welcome_channel:
        await welcome_channel.send(f'Goodbye {member.name}! :wave: We will miss you.')

    # Send dm's to the leaving member
    try:
        await member.send(f'Goodbye, {member.name}! We\'re sad to see you leave. If you ever want to come back, you\'re always welcome!')
    except:
        pass  # If the member has DMs disabled or the bot cannot send messages, it will ignore the error

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if message.content.startswith("Hello"):
    await message.channel.send("Hello! Hey there.")

  if message.content.startswith("Quote"):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith("!funfact"):
    fun_fact = random.choice(fun_facts)
    await message.channel.send(fun_fact)

#Check for discourage words and send uplifting message
  if any(word in message.content for word in frustrating_words): 
      await message.channel.send(random.choice(uplifting_words))

# Handle adding new encouraging message to database
  if message.content.startswith("!new"):
      encouraging_message = message.content.split("!new ", 1)
      if len(encouraging_message) > 1:
          encouraging_message = encouraging_message[1]
          update_encouragements(encouraging_message)    
          uplifting_feedback = "Your positive message has been added to the collection!"
          await message.channel.send(uplifting_feedback)
      else:
          await message.channel.send("Invalid format for adding an encouraging message.")

# Handle deleting encouraging message from database.
  if message.content.startswith("!del"):
      try:
          index = int(message.content.split("!del", 1)[1])
          delete_encouragement(index)
          uplifting_feedback = "Encouraging message deleted successfully!"
          await message.channel.send(uplifting_feedback)
      except ValueError:
          await message.channel.send("Invalid index. Please enter a valid integer.")

#Moderation Commands #Kick
  if message.content.startswith('!kick'):
    # Check if the user has permissions to kick members
    if message.author.guild_permissions.kick_members:
        # Get the mentioned member to kick
        if message.mentions:
            member = message.mentions[0]
            # Kick the member
            await member.kick(reason="Kicked by command")
            await message.channel.send(f'{member.display_name} has been kicked!')
        else:
            await message.channel.send('Please mention the user you want to kick.')
    else:
        await message.channel.send('You do not have permission to kick members.')

#Ban Command
  if message.content.startswith('!ban'):
      # Check if the user has permissions to ban members
      if message.author.guild_permissions.ban_members:
          # Get the mentioned member to ban
          if message.mentions:
              member = message.mentions[0]
              # Ban the member
              await message.guild.ban(member, reason="Banned by command")
              await message.channel.send(f'{member.display_name} has been banned!')
          else:
              await message.channel.send('Please mention the user you want to ban.')
      else:
          await message.channel.send('You do not have permission to ban members.')  
#Unban Command
  if message.content.startswith('!unban'):
    # Check if the user has permissions to unban members
    if message.author.guild_permissions.ban_members:
        # Get the mentioned user to unban
        if message.content.split(' ')[1:]:
            user_id = int(message.content.split(' ')[1])
            banned_users = await message.guild.bans()
            for ban_entry in banned_users:
                if ban_entry.user.id == user_id:
                    # Unban the user
                    await message.guild.unban(ban_entry.user)
                    await message.channel.send(f'{ban_entry.user.name} has been unbanned!')
                    return
            await message.channel.send('User not found in ban list.')
        else:
            await message.channel.send('Please provide the ID of the user you want to unban.')
    else:
        await message.channel.send('You do not have permission to unban members.')

#Server rules command
  if message.channel.id == RULES_CHANNEL_ID and message.content.lower() == "!rules":
     # Define the rules text
     rules = '''
     **Welcome to We Bare Broz Server!**

     1. **Bros, Respect the Brotherhood:** Treat each other with respect and keep the bro code alive.

     2. **Unwind Territory:** No room for drama or stress, bros. This is our sanctuary to relax, game, code, and unwind.

     3. **Meme Hub:** Bring on the memes, jokes, and good times. Keep it hilarious but avoid anything too wild.

     4. **Bare Bros Together:** Brotherhood runs deep in this server. Stand by your bros through thick and thin.

     5. **Good deed Only:** Keep it positive, bros. No time for negativity.

     6. **Level Up Together:** Share your gaming triumphs, programming hacks, and learning adventures.

     7. **Be Famed:** Let's make this hangout legendary. Whether conquering new games or crushing coding challenges, let's do it together!

     It's Homeis time, let's play, code, and learn together!

     A message from the creator: These rules are just for manners and gestures. You'll know how we behave in group chats.
     **Thank you for joining We Bare Broz Server!**
     '''
     # Create an embed with the rules content
     embed = discord.Embed(title="Rules", description=rules, color=discord.Color.red())

#Poll Creating Command 
  if message.content.startswith("!poll"):
        # Split the message content to get the question and options
        poll_content = message.content.split("!poll", 1)[1].strip()
        question, *options = poll_content.split("|")

        # Remove leading and trailing spaces from options
        options = [option.strip() for option in options]

        # Create the poll embed
        poll_embed = discord.Embed(title=question, description="React to vote", color=0x00ff00)

        # Add options as fields in the embed
        for index, option in enumerate(options):
            poll_embed.add_field(name=f"Option {index+1}", value=option, inline=False)

        # Send the poll message
        poll_message = await message.channel.send(embed=poll_embed)

        # Add reactions to the poll message for each option
        for index, option in enumerate(options):
            await poll_message.add_reaction(chr(0x1f1e6 + index))  # Adds unicode reactions 1️⃣, 2️⃣, etc.

#Help Command
  if message.content.startswith('!assist'):
    embed = discord.Embed(title="Bot Commands", description="Here is a list of available commands:", color=0x00ff00)

    embed.add_field(name="General Commands",
                    value="`quote` - Get a random quote.\n"
                          "`!funfact` - Get a random fun fact.\n"
                          "`!new Your_encouraging_message` - Add a new encouraging message to the bot's collection.\n"
                          "`!del index` - Delete an encouraging message from the bot's collection by its index number.",
                    inline=False)

    embed.add_field(name="Moderation Commands",
                    value="`!kick @user` - Kick a user from the server. (Requires appropriate permissions).\n"
                          "`!ban @user` - Ban a user from the server. (Requires appropriate permissions).\n"
                          "`!unban user_id` - Unban a user from the server by their ID. (Requires appropriate permissions).\n"
                          "`!rules` - Display server rules. (Only works in the rules channel).",
                    inline=False)

    embed.add_field(name="Utility Commands",
                    value="`!poll question | option1 | option2 | ...` - Create a poll with multiple options.\n"
                          "`!assist` - Display this list of commands.\n"
                          "`!botinfo` - Display bot information.\n"
                          "`!clear number` - Clear a specified number of messages. (Requires appropriate permissions).\n"
                          "`!weather location` - Get the current weather for a location.",
                    inline=False)

    embed.add_field(
    name="Engagement Commands",
    value="`!meme [subreddit_name]` - Fetch a random meme from a specified subreddit. If no subreddit is provided, it defaults to 'memes'.\n"
    "`!monitor_subreddit subreddit_name` - Monitor a subreddit for new posts.\n"
    "`!stop_monitoring_subreddit subreddit_name` - Stop monitoring a subreddit for new posts.\n"
    "`!recommend_movie` - Get a recommendation for a movie.\n"
    "`!recommend_tvshow` - Get a recommendation for a TV show.\n"
    "`!e <python_code>` - Execute Python code directly within Discord.",
    inline=False)

    await message.channel.send(embed=embed)

#Bot Info Command
  if message.content.startswith('!botinfo'):
    embed = discord.Embed(title="Bot_Information", color=discord.Color.red())
    embed.add_field(name="Name", value=bot.user, inline=False)
    embed.add_field(name="Creator", value="ArunKumar", inline=False)
    embed.add_field(name="Model", value="Basic", inline=False)
    embed.add_field(name="Description", value="A basic bot that provides information.", inline=False)
    await message.channel.send(embed=embed)

#Clear Command
  if message.content.startswith( prefix + "clear"):
     if message.author.guild_permissions.manage_messages:
       try:
          amount = int(message.content.split()[1])
          if 0 < amount <= 100:
              await message.channel.purge(limit=amount + 1) # +1 to include the command itself
              await message.channel.send(f"{amount} messages cleared by {message.author.mention}.")
          else:
              await message.channel.send("Please provide a number between 1 and 100.")
       except IndexError:
          await message.channel.send("Please provide the number of messages to clear.")
       except ValueError:
          await message.channel.send("Invalid number of messages provided.")
     else:
          await message.channel.send("You do not have permission to use this command.")

#weather command
  if message.content.startswith('!weather'):
        location = message.content.split(' ', 1)[1]
        weather_data = get_weather(location)
        if weather_data:
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            await message.channel.send(f"The weather in {location} is {weather_description} with a temperature of {temperature}°C.")
        else:
            await message.channel.send("Sorry, I couldn't retrieve the weather information for that location.")
#Userinfo Command
  if message.content.startswith('!userinfo'):
        member = message.author
        roles = [role.name for role in member.roles]

        embed = discord.Embed(
            title="User Information",
            color=member.color
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar_url)
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined Discord", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

        guild = message.guild
        member = guild.get_member(message.author.id)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)

        embed.add_field(name="Roles", value=", ".join(roles), inline=False)

        await message.channel.send(embed=embed)

#Meme Command
# Check if the message starts with !meme command
  if message.content.startswith('!meme'):
        # Extract the subreddit name from the command
        subreddit_name = message.content.split(' ', 1)[1] if len(message.content.split(' ', 1)) > 1 else 'memes'

        # Fetch a random meme from the specified subreddit
        meme = fetch_random_meme(subreddit_name)

        # Send the meme to the Discord channel
        await message.channel.send(meme)

#post from subreddit's
  if message.content.startswith('!monitor_subreddit'):
        subreddit_name = message.content.split(' ', 1)[1].lower() if len(message.content.split(' ', 1)) > 1 else None
        if subreddit_name:
            await message.channel.send(f"Monitoring r/{subreddit_name} for new posts...")
            monitored_subreddits[subreddit_name] = True
            subreddit = reddit.subreddit(subreddit_name)
            for submission in subreddit.stream.submissions():
                if not monitored_subreddits[subreddit_name]:
                    await message.channel.send(f"Stopped monitoring r/{subreddit_name}.")
                    break
                await message.channel.send(f"New post in r/{subreddit_name}: {submission.title}\n{submission.url}")
        else:
            await message.channel.send("Please specify a subreddit to monitor. Usage: !monitor_subreddit [subreddit_name]")

  if message.content.startswith('!stop_monitoring_subreddit'):
        subreddit_name = message.content.split(' ', 1)[1].lower() if len(message.content.split(' ', 1)) > 1 else None
        if subreddit_name and subreddit_name in monitored_subreddits:
            monitored_subreddits[subreddit_name] = False
            await message.channel.send(f"Stopped monitoring r/{subreddit_name}.")
        else:
            await message.channel.send("Subreddit is not being monitored.")
# Check if the message is in the movies channel
  if message.channel.id == MOVIES_CHANNEL_ID and message.content.startswith('!recommend_movie'):
        recommended_movie = random.choice(movies_list)
        await message.channel.send(f"I would recommend you watch **{recommended_movie}**!")

  if message.channel.id == TV_SHOWS_CHANNEL_ID and message.content.startswith('!recommend_tvshow'):
        recommended_tv_show = random.choice(tv_shows)
        await message.channel.send(f"I would recommend you to watch **{recommended_tv_show}**!")

#py command
  if message.channel.id == BOT_COMMANDS_ID and message.content.startswith('!python'):
    code = message.content[8:]  # Extract code from message content

    # Execute Python code using subprocess
    try:
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            output = result.stdout.strip()
        else:
            output = result.stderr.strip()
    except subprocess.TimeoutExpired:
        output = "Timeout: Execution took too long."
    except subprocess.CalledProcessError as e:
        output = f"Error: {e}"
    except Exception as e:
        output = f"Error: {e}"

    # Send output back to Discord
    await message.channel.send(f"```python\n{output}\n```")

#Run the bot
my_secret = os.environ['BOT_KEY']
bot.run(my_secret)