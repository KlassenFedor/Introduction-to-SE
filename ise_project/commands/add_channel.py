from telethon import utils
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import *
from database import Channel


async def main_command(client, tokens):
    try:
        channel = tokens[0]
        if len(tokens) == 2:
            if tokens[1] == '-p':
                try:
                    await client(ImportChatInviteRequest(tokens[1].split('/')[-1]))
                    await add_entity_to_db(tokens[0], client)
                except Exception as e:
                    message = 'Что-то пошло не так'
                    await client.send_message(message)
        await client(JoinChannelRequest(channel))
        await add_entity_to_db(tokens[0], client)
    except Exception as e:
        message = 'Что-то пошло не так'
        if e == ChannelPrivateError:
            message = 'Этот канал приватный, вам следует прислать ссылку-приглашение, чтобы присоединиться'
        await client.send_message(message)


async def add_entity_to_db(entity, client):
    try:
        channel_name = utils.get_display_name(entity)
        new_channel = Channel(channel_id=entity, name=channel_name)
        new_channel.Save()
    except Exception as e:
        message = 'Что-то пошло не так'
        await client.send_message(message)
