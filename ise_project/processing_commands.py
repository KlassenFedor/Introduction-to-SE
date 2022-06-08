import importlib

command = ''

commands_list = '''/info /info_commands /info_command /channels /ban_words /messages_types 
                    /add_channel /delete_channel 
                    /add_ban_word /delete_ban_word /add_type /delete_type /set_defaults 
                    /clear_ban_list /white_mode /add_white_word'''.split()
hashtags = '''-ht'''.split()


async def call_command(current_command):
    module = importlib.import_module('commands.{}'.format(current_command))
    await module.main_command()


async def process_command(current_command):
    tokens = current_command.split()
    if tokens[0][0] != '/':
        message = "It's not a command"
    else:
        if tokens[0] in commands_list:
            current_token = tokens[0]

            # info commands
            if current_token == '/info':
                if check_info(tokens):
                    await call_command('info')
                else:
                    message = 'Incorrect command'

            if current_token == '/info_commands':
                if check_info_commands(tokens):
                    await call_command('info_commands')
                else:
                    message = 'Incorrect command'

            if current_token == '/info_command':
                if check_info_command(tokens):
                    await call_command('info_command')
                else:
                    message = 'Incorrect command'

            if current_token == '/channels':
                if check_channels(tokens):
                    await call_command('channels')
                else:
                    message = 'Incorrect command'

            if current_token == '/ban_words':
                if check_ban_words(tokens):
                    await call_command('ban_words')
                else:
                    message = 'Incorrect command'

            # channel commands
            if current_token == '/messages_types':
                if check_messages_types(tokens):
                    await call_command('messages_types')
                else:
                    message = 'Incorrect command'

            if current_token == '/add_channel':
                if check_is_channel_token_correct(tokens):
                    await call_command('add_channel')
                else:
                    message = 'Incorrect command'

            if current_token == '/delete_channel':
                if check_is_channel_token_correct(tokens):
                    await call_command('delete_channel')
                else:
                    message = 'Incorrect command'

            # filtration commands
            if current_token == '/add_ban_word':
                if check_channel_and_word_with_hashtag(tokens):
                    await call_command('add_ban_word')
                else:
                    message = 'Incorrect command'

            if current_token == '/delete_ban_word':
                if check_channel_and_word_with_hashtag(tokens):
                    await call_command('delete_ban_word')
                else:
                    message = 'Incorrect command'

            if current_token == '/add_type':
                if check_channel_and_word(tokens):
                    await call_command('add_type')
                else:
                    message = 'Incorrect command'

            if current_token == '/delete_type':
                if check_channel_and_word(tokens):
                    await call_command('delete_type')
                else:
                    message = 'Incorrect command'

            if current_token == '/set_defaults':
                if check_channel_and_word(tokens):
                    await call_command('set_defaults')
                else:
                    message = 'Incorrect command'

            if current_token == '/clear_ban_list':
                if check_channel_and_word(tokens):
                    await call_command('clear_ban_list')
                else:
                    message = 'Incorrect command'

            if current_token == '/white_mode':
                if check_channel_and_word(tokens):
                    await call_command('white_mode')
                else:
                    message = 'Incorrect command'

            if current_token == '/add_white_word':
                if check_channel_and_word_with_hashtag(tokens):
                    await call_command('add_white_word')
                else:
                    message = 'Incorrect command'

            if current_token == '/delete_white_word':
                if check_channel_and_word_with_hashtag(tokens):
                    await call_command('delete_white_word')
                else:
                    message = 'Incorrect command'

        else:
            message = "This command doesn't exists"


def check_hashtag(token):
    if token[0] == '-':
        if token not in hashtags:
            return False
        else:
            return True
    return False


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


def check_channel_and_word(tokens):
    if len(tokens) != 3:
        return False
    if not (check_is_a_simple_token(tokens[1]) and check_is_a_simple_token(tokens[2])):
        return False
    return True


def check_channel_and_word_with_hashtag(tokens):
    if len(tokens) != 3 or len(tokens) != 4:
        return False
    if not (check_is_a_simple_token(tokens[1]) and check_is_a_simple_token(tokens[2])):
        return False
    if len(tokens) == 4:
        if not check_hashtag(tokens[3]):
            return False
    return True
