async def send_message_to_new_user(user, client):
    message = '''Это агрегатор телеграм-каналов, для получения информации посетите
                 https://github.com/KlassenFedor/Introduction-to-SE'''
    await client.send_message(message)
