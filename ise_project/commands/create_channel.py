from telethon.tl import functions


async def main_command(client, tokens):
    message = ''
    try:
        result = client(functions.channels.CreateChannelRequest(
            title='Aggregator',
            about='''Данный канал будет агрегировать интересующие вас сообщения,
                     вы будете иметь все права администратора и возможность добавлять новых пользователей'''
        ))
        message = 'Aggregator'
        await client.send_message(message)
    except Exception as e:
        message = 'Что-то пошло не так'
        await client.send_message(message)
