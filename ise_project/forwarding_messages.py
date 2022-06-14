from telethon.sync import events

from commands.info import main_command
from commands.send_info_to_unknown_user import send_message_to_new_user
from database import Channel
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
        else:
            await send_message_to_new_user(sender, client)


async def check_if_the_sender_being_tracked(sender):
    channels = Channel.get()
    for channel in channels:
        if channel.channel_id == sender:
            return True
    return False


async def filtrate_message(message):
    pass
