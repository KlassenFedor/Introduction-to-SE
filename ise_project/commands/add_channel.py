from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import *


async def main_command(client, tokens):
    try:
        channel = tokens[0]
        if len(tokens) == 2:
            if tokens[1] == '-p':
                try:
                    await client(ImportChatInviteRequest(tokens[1].split('/')[-1]))
                except Exception as e:
                    message = 'Что-то пошло не так'
                    await client.send_message(message)
        await client(JoinChannelRequest(channel))
    except Exception as e:
        message = 'Что-то пошло не так'
        if e == ChannelPrivateError:
            message = 'Этот канал приватный, вам следует прислать ссылку-приглашение, чтобы присоединиться'
        await client.send_message(message)
