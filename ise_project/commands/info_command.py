async def main_command(client, tokens):
    message = 'К сожалению, команда не найдена'
    if tokens[0] == '/info' or 'info':
        message = 'возвращает краткую информацию о данном агрегаторе'
    if tokens[0] == '/info_command' or 'info_command':
        message = 'возвращает описание интересующей команды'
    if tokens[0] == '/info_commands' or 'info_commands':
        message = 'возвращает список команд'
    if tokens[0] == '/add_ban_word' or 'add_ban_word':
        message = 'добавляет бан-слово для заданного канала'
    if tokens[0] == '/add_channel' or 'add_channel':
        message = 'добавляет канал в отслеживаемые'
    if tokens[0] == '/add_type' or 'add_type':
        message = 'добавляет сортировку по типу сообщений для заданного канала'
    if tokens[0] == '/add_white_word' or 'add_white_word':
        message = 'добавлят слово в белый список для заданного канала'
    if tokens[0] == '/ban_words' or 'ban_words':
        message = 'выводит список млов из бан-листа для данного канала'
    if tokens[0] == '/channels' or 'channels':
        message = 'выводит список отслеживаемых каналов'
    if tokens[0] == '/clear_ban_list' or 'clear_ban_list':
        message = 'очищает список заблокированных слов для заданного канала'
    if tokens[0] == '/delete_ban_word' or 'delete_ban_word':
        message = 'удаляет бан-слово из бан-листа для данного канала'
    if tokens[0] == '/delete_type' or 'delete_type':
        message = 'удалят тип сообщений из отслеживаемых для данного канала'
    if tokens[0] == '/delete_white_word' or 'delete_white_word':
        message = 'удаляет слово из белого списка'
    if tokens[0] == '/messages_types' or 'messages_types':
        message = 'выводит список типов сообщений, отслеживаемых для данного канала'
    if tokens[0] == '/set_defaults' or 'set_defaults':
        message = 'устанавливает стандартные настройки для заданного канала'
    if tokens[0] == '/white_mode' or 'white_mode':
        message = 'переводит канал в режим работы белого списка'

    await client.send_message(message)
