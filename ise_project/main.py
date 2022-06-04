from telethon.sync import TelegramClient, events
from processing_commands import process_command
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, int(api_id), api_hash)


@client.on(events.NewMessage())
async def event_handler(event):
    await process_command(event.message)
