from telethon.sync import events

from database import Channel, ChannelBanWord, BanWord, ChannelWhiteWord, WhiteWord, ChannelMessageType, MessageType
from main import client, module, main_account


@client.on(events.NewMessage())
async def event_handler(event):
    sender = await client.get_entity(event.message.from_id.user_id)
    if sender == main_account:
        await module.process_command(event.message)
    else:
        is_sender_is_tracked = await check_if_the_sender_being_tracked(sender)
        if is_sender_is_tracked:
            if filtrate_message(event.message):
                await client.forward_messages(main_account, event.message)


async def check_if_the_sender_being_tracked(sender):
    channels = Channel.get()
    for channel in channels:
        if channel.channel_id == sender:
            return True
    return False


async def get_message_types(message):
    pass


async def has_ban_words(message, ban_words):
    pass


async def has_white_words(message, white_words):
    pass


async def has_message_types(types_in_message, channel_types):
    pass


async def filtrate_message(message):
    sender = await client.get_entity(message.from_id.user_id)
    message_text = message.text
    message_types_in_message = get_message_types(message)

    ban_words_ids = ChannelBanWord.get(ChannelBanWord.channel == sender)
    ban_words = []
    for ban_word_id in ban_words_ids:
        ban_words = BanWord.get(BanWord.get_id == ban_word_id).select(BanWord.word)

    white_words_ids = ChannelWhiteWord.get(ChannelWhiteWord.channel == sender)
    white_words = []
    for white_word_id in white_words_ids:
        white_words = WhiteWord.get(WhiteWord.get_id == white_word_id).select(WhiteWord.word)

    message_types_ids = ChannelMessageType.get(ChannelMessageType.channel == sender)
    message_types = []
    for message_type_id in message_types_ids:
        message_types = MessageType.get(WhiteWord.get_id == message_type_id).select(MessageType.type)

    if has_white_words(message_text, white_words):
        return True
    if has_ban_words(message_text, ban_words):
        return False
    if not has_message_types(message_types_in_message, message_types):
        return False

    return True

