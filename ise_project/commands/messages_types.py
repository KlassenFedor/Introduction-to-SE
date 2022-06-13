import database
from commands.commands_helper import check_is_channel_exists


async def main_command(client, tokens):
    message = ''
    if check_is_channel_exists(tokens[0]):
        message = 'Такого канала не существует'
        await client.send_message(message)
        return
    channel_id = database.Channel.get(database.Channel.name == tokens[0]).id
    message_type_ids = list(database.ChannelMessageType.get(database.ChannelMessageType.channel == channel_id).MessageType)
    message = ''
    for message_type in message_type_ids:
        message += database.MessageType.get(database.MessageType.id == message_type).type + ' '

    await client.send_message(message)
