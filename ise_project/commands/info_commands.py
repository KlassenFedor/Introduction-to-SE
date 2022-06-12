async def main_command(client, tokens):
    message = '''Ниже вы можете увидеть полный перечень доступных команд,
                 для получения подробной информации по команде используй: /info_command 
                 
                 /info
                 /info_command
                 /info_commands
                 /channels
                 /ban_words
                 /messages_types
                 /add_channel
                 /delete_channel
                 /add_ban_word
                 /delete_ban_word
                 /add_type
                 /delete_type
                 /set_defaults
                 /clear_ban_list
                 /white_mode
                 /add_white_word
                 /delete_white_word
                 '''
    await client.send_message(message)
