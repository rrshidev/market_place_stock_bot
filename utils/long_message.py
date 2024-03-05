def long_message(table):

    selected_rows = table[0:]
    # print(selected_rows)

    formatted_table = ''
    messageTable = []
    for row in selected_rows:
        formatted_row = ' | '.join(row)
        formatted_table += f'{formatted_row}\n'

    if len(formatted_table) > 4096:

        for part in range(0, len(formatted_table), 4096):
            messageTable.append(formatted_table[part:part+4096])

    # print(messageTable)
    return messageTable


import asyncio
async def send_long_message(bot, chat_id, message_text, parse_mode="HTML", reply_markup=None):
    max_message_length = 4096  # Максимальная длина сообщения
    chunks = [message_text[i:i+max_message_length] for i in range(0, len(message_text), max_message_length)]

    for chunk in chunks:
        await bot.send_message(chat_id, chunk, parse_mode=parse_mode, reply_markup=reply_markup)
        await asyncio.sleep(1)  # Пауза между отправкой частей сообщения
