from commands.commands_helper import *


async def main_command(client, tokens):
    channel = tokens[0]
    ban_word = tokens[1]
    hashtag = tokens[2]
    message = ''
    if not check_is_channel_exists(tokens[0]):
        message = 'Такого канала нет в отслеживаемых'
        await client.sent_message(message)
        return
    if check_is_ban_word_exists(ban_word, channel):
        message = 'Это слово уже существует'
        await client.sent_message(message)
        return

    message = 'Слово добавлено, больше вы его не увидите в сообщениях от данного канала'
    await client.sent_message(message)

