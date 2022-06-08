from telethon.sync import TelegramClient, events
import configparser
import importlib


config = configparser.ConfigParser()
config.read("config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
main_account = config['Telegram']['main_account']

client = TelegramClient(username, int(api_id), api_hash)
module = importlib.import_module('processing_commands')


@client.on(events.NewMessage())
async def event_handler(event):
    await module.process_command(event.message)


client.start()
client.send_message(main_account, 'Hello! Start of work.')
client.run_until_disconnected()
