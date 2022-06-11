from database import Channel


async def main_command(client):
    channels = Channel.get()
    message = ''

    for channel in channels:
        message += channel.name + '/n'

    await client.send_message(message)
