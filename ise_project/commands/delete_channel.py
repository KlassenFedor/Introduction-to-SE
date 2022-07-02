import logging

from telethon.errors import ChannelPrivateError
from telethon.tl.functions.channels import LeaveChannelRequest
from database import Channel


async def main_command(client, tokens):
    channels = Channel.get()
    channel_exists = False
    for channel in channels:
        if channel.channel_id == tokens[0]:
            channel_exists = True
            break
    if channel_exists:
        try:
            await client(LeaveChannelRequest(tokens[0]))
            await delete_entity_from_db(tokens[0], client)
            message = 'Канал был успешно удален'
            await client.send_message(message)
        except Exception as e:
            message = 'Не удалось удалить канал'
            if e == ChannelPrivateError:
                await client.delete_dialog(tokens[0])
                await delete_entity_from_db(tokens[0], client)
            else:
                await client.send_message(message)


async def delete_entity_from_db(channel_id, client):
    try:
        channel = Channel.get(Channel.channel_id == channel_id)
        channel.delete_instance()
    except Exception as e:
        logging.error('Не удалось удалить из базы данных' + ' ' + str(e))
