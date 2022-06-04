from commands.ban_words import get_ban_words
from commands.info import get_info
from commands.info_commands import get_all_commands_info
from commands.info_command import get_command_info
from commands.channels import get_all_channels
from commands.messages_types import get_messages_types
from commands.add_channel import add_channel
from commands.delete_channel import delete_channel

command = ''

commands_list = '''/info /info_commands /info_command /channels /ban_words /messages_types 
                    /add_channel /delete_channel 
                    /add_ban_word /delete_ban_word /add_type /delete_type /set_defaults 
                    /clear_ban_list /white_mode /add_white_word'''.split()
hashtags = '''-ht'''.split()


async def process_command(current_command):
    tokens = current_command.split()
    if tokens[0][0] != '/':
        message = "It's not a command"
    else:
        if tokens[0] in commands_list:
            current_token = tokens[0]
            if current_token == '/info':
                if check_info(tokens):
                    await get_info()
                else:
                    message = 'Incorrect command'

            if current_token == '/info_commands':
                if check_info_commands(tokens):
                    await get_all_commands_info()
                else:
                    message = 'Incorrect command'

            if current_token == '/info_command':
                if check_info_command(tokens):
                    await get_command_info(tokens[1])
                else:
                    message = 'Incorrect command'

            if current_token == '/channels':
                if check_channels(tokens):
                    await get_all_channels()
                else:
                    message = 'Incorrect command'

            if current_token == '/ban_words':
                if check_ban_words(tokens):
                    await get_ban_words(tokens)
                else:
                    message = 'Incorrect command'

            if current_token == '/messages_types':
                if check_messages_types(tokens):
                    await get_messages_types(tokens)
                else:
                    message = 'Incorrect command'

            if current_token == '/add_channel':
                if check_is_channel_token_correct(tokens):
                    await add_channel(tokens[1])
                else:
                    message = 'Incorrect command'

            if current_token == '/delete_channel':
                if check_is_channel_token_correct(tokens):
                    await delete_channel(tokens[1])
                else:
                    message = 'Incorrect command'

        else:
            message = "This command doesn't exists"


def find_and_check_hashtags(tokens):
    for token in tokens:
        if token[0] == '-':
            if token not in hashtags:
                message = "Incorrect hashtag"


def check_is_a_simple_token(token):
    if len(token) > 0:
        if token[0] != '-' and token[0] != '/':
            return True
    return False


def check_info(tokens):
    if len(tokens) != 1:
        return False
    return True


def check_info_commands(tokens):
    if len(tokens) != 1:
        return False
    return True


def check_info_command(tokens):
    if len(tokens) != 2:
        return False
    if not check_is_a_simple_token(tokens[1]):
        return False
    return True


def check_channels(tokens):
    if len(tokens) != 1:
        return False
    return True


def check_ban_words(tokens):
    if len(tokens) != 2:
        return False
    if not check_is_a_simple_token(tokens[1]):
        return False
    return True


def check_messages_types(tokens):
    if len(tokens) != 2:
        return False
    if not check_is_a_simple_token(tokens[1]):
        return False
    return True


def check_is_channel_token_correct(tokens):
    if len(tokens) != 2:
        return False
    if not check_is_a_simple_token(tokens[1]):
        return False
    return True
