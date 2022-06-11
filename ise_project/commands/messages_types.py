import database


async def main_command(client, channel):
    channel_id = database.Channel.get(database.Channel.name == channel).id
    message_type_ids = list(database.ChannelMessageType.get(database.ChannelMessageType.channel == channel_id).MessageType)
    message = ''
    for message_type in message_type_ids:
        message += database.MessageType.get(database.MessageType.id == message_type).type + ' '

    await client.send_message(message)
