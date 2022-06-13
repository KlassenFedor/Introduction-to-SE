from database import Channel


def check_is_channel_exists(channel):
    current_channel = Channel.get(Channel.channel_id == channel)
    if len(current_channel) == 0:
        return False
    return True
