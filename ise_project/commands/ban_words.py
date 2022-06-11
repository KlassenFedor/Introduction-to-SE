from database import BanWord, ChannelBanWord, Channel


async def main_command(client, channel):
    channel_id = Channel.get(Channel.name == channel).id
    ban_words_ids = list(ChannelBanWord.get(ChannelBanWord.channel == channel_id).BanWord)
    message = ''
    for ban_word in ban_words_ids:
        message += BanWord.get(BanWord.id == ban_word).word + ' '

    await client.send_message(message)
