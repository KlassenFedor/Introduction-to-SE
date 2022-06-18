from telethon.sync import events
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import *

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
    my_channels = Channel.get()
    for channel in my_channels:
        if channel.channel_id == sender:
            return True
    return False


async def get_message_types(message):
    filters = [InputMessagesFilterPhotos(),
               InputMessagesFilterVideo(),
               InputMessagesFilterDocument(),
               InputMessagesFilterVoice(),
               InputMessagesFilterUrl()]
    types = []
    all_types = ['photo', 'video', 'document', 'voice', 'url']
    channel = await client.get_entity(message.chat_id)
    message_id = message.id
    counter = 0
    for my_filter in filters:
        result = client(SearchRequest(
            peer=channel,
            q='',
            filter=my_filter,
            min_date=None,
            max_date=None,
            offset_id=0,
            add_offset=0,
            limit=1,
            max_id=message_id,
            min_id=message_id,
            hash=message.hash
        ))
        if len(result) == 1:
            types.append(all_types[counter])
    return types


async def has_ban_words(message, ban_words):
    all_words = message.split()
    for word in all_words:
        if word in ban_words:
            return True
    return False


async def has_white_words(message, white_words):
    all_words = message.split()
    for word in all_words:
        if word in white_words:
            return True
    return False


async def has_message_types(types_in_message, channel_types):
    for type_in_message in types_in_message:
        if type_in_message in channel_types:
            return True
    return False


async def filtrate_message(message):
    sender = await client.get_entity(message.from_id.user_id)
    message_text = message.text
    message_types_in_message = await get_message_types(message)

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

