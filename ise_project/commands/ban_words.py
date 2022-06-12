from commands.commands_helper import check_is_channel_exists
from database import BanWord, ChannelBanWord, Channel


async def main_command(client, tokens):
    message = ''
    if check_is_channel_exists(tokens[0]):
        message = 'Такого канала не существует'
        await client.send_message(message)
        return
    channel_id = Channel.get(Channel.name == tokens[0]).id
    ban_words_ids = list(ChannelBanWord.get(ChannelBanWord.channel == channel_id).BanWord)
    for ban_word in ban_words_ids:
        message += BanWord.get(BanWord.id == ban_word).word + ' '

    await client.send_message(message)
