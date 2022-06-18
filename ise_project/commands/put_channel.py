from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest


async def main_command(client, tokens):
    message = ''
    if tokens[0][0:16] == 'https://t.me/join':
        try:
            client(ImportChatInviteRequest(tokens[0].split('/')[-1]))
        except Exception as e:
            message = 'Не удалось присоединиться к каналу'
            await client.send_message(message)
    else:
        try:
            client(JoinChannelRequest(tokens[0]))
        except Exception as e:
            message = 'Не удалось присоединиться к каналу'
            await client.send_message(message)
