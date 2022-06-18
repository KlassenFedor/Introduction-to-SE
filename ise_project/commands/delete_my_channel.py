from telethon.tl import functions


async def main_command(client, tokens):
    message = ''
    try:
        result = client(functions.channels.DeleteChannelRequest(
            channel=tokens[0]
        ))
        message = 'Канал удален'
        await client.send_message(message)
    except Exception as e:
        message = 'Не удалось удалить канал'
        await client.send_message(message)