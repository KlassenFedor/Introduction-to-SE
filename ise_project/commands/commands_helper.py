from database import Channel, BanWord, ChannelBanWord


def check_is_channel_exists(channel):
    current_channel = Channel.get(Channel.channel_id == channel)
    if len(current_channel) == 0:
        return False
    return True


def check_is_ban_word_exists(ban_word, channel):
    existing_ban_word = BanWord.get(BanWord.word == ban_word)
    matched_ban_word_and_channel = ChannelBanWord.get(ChannelBanWord.get_id == existing_ban_word.id)
    if matched_ban_word_and_channel is None:
        return False
    return True
