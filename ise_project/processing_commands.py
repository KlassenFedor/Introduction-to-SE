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
            pass
        else:
            message = "This command doesn't exists"


def find_and_check_hashtags(tokens):
    for token in tokens:
        if token[0] == '-':
            if token not in hashtags:
                message = "Incorrect hashtag"
