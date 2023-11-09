# Import the discord.py library
import discord

# Create a client object
client = discord.Client()

# Define a bot token (replace with your own)
TOKEN = "your-bot-token-here"

# Define a method that accepts a message and a callback
def ask(message, callback):
  # Send the message to the user
  await message.channel.send(message)
  # Wait for a response
  response = await client.wait_for("message", check=lambda m: m.author == message.author and m.channel == message.channel)
  # Pass the response to the callback
  callback(response)

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
  # Print a message to the console
  print(f"{client.user} has connected to Discord!")

# Define an event handler for when the bot receives a message
@client.event
async def on_message(message):
  # Ignore messages from the bot itself
  if message.author == client.user:
    return
  # If the message starts with "!hello"
  if message.content.startswith("!hello"):
    # Greet the user
    await message.channel.send(f"Hello, {message.author}!")
    # Ask the user a question and print the answer to the console
    ask("How are you today?", lambda response: print(f"{message.author} said: {response.content}"))

# Run the bot using the token
client.run(TOKEN)
