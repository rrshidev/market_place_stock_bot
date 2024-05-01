import logging
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from getRequests.getCategories import get_categories
from getRequests.getCheckNumber import get_check_number
from getRequests.getProductData import get_product_data
from getRequests.getTargetStock import get_names_of_product
from getRequests.getSizes import get_sizes
from setRequests.setSell import set_sell
from stock import get_stock
from markups import buy_sell_menu, menu_markup, menu_markup_names_of_products, menu_markup_product, sell_type_buttons, size_buttons
from Secrets.config import telegram_token, sheet_id
from utils.long_message import long_message, send_long_message
from Secrets.config import path_to_photos



API_TOKEN = telegram_token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
user_sessions = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Выберите действие:", reply_markup=menu_markup())


@dp.callback_query_handler(lambda call: True)
async def process_callback(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    
    if callback_query.data == 'check_balance':
        table = await get_stock()
        # values = worksheet.col_values(1) 
        chat_id = callback_query.message.chat.id
        messages = long_message(table=table)
        for message in messages:
            await bot.send_message(
                chat_id=chat_id,
                text=message,
            )
    
    if callback_query.data == 'check_balance_product':
        category = await get_categories()
        chat_id = callback_query.message.chat.id
        message = 'Выбери категорию товара:\n\n'
    # messages = long_message(table=category)
        await bot.send_message(
            chat_id=chat_id,
            text=message,
            reply_markup=menu_markup_product(category=category)
        )

    if callback_query.data.startswith('category|'):
        category = callback_query.data.split('|')[1]
        globalList = await get_names_of_product(category=category)
        names = globalList[0]
        index = globalList[1]
        # print(names)
        chat_id = callback_query.message.chat.id
        message = f'Выбери позицию:\n\n '
        for name, index in zip(names, index):

            await bot.send_message(
                chat_id=chat_id,
                text=message,
                reply_markup=menu_markup_names_of_products(name=name, index=index)
            )
    
    if callback_query.data.startswith('product|'):
        product_index = callback_query.data.split('|')[1]
        chat_id = callback_query.message.chat.id
        product_data_list = await get_product_data(product_index=product_index, flag=False)
        product_data = product_data_list[0]
        flag = product_data_list[1]
        print('FLAG2-->',flag)
        if flag == True:
            photo_name = product_data_list[2]
            product_name = product_data_list[3]
            product_index = product_data_list[4]

            with open(f'{path_to_photos}{photo_name}', 'rb') as f:
                photo = f.read()

                await bot.send_message(
                    chat_id=chat_id,
                    text=product_data,
                )
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=photo, 
                    reply_markup=buy_sell_menu(product_index)
                )
        else:
            product_name = product_data_list[2]
            product_index = product_data_list[3]
            await bot.send_message(
                chat_id=chat_id,
                text=product_data,
                reply_markup=buy_sell_menu(product_index)
            )

    if callback_query.data.startswith('sell'):
        await set_sell()
        phrase = 'You add information to the table! Nice!'
        await bot.send_message(
            chat_id=chat_id,
            text=phrase,
        )

    if callback_query.data.startswith('new_check|'):
        product_index = callback_query.data.split('|')[1]
        product_data = await get_product_data(product_index=product_index, flag=False)
        chat_id = callback_query.message.chat.id
        # sizes = await get_sizes(product_name)
        product_flag = product_data[1]
        if product_flag == True:
            sizes = product_data[5]
            product_name = product_data[3]
        else:
            sizes = product_data[4]
            product_name = product_data[2]    
       
        phrase = f'Новый чек: {product_name}\n\nВыбери размер:'

        
        await bot.send_message(
            chat_id=chat_id,
            text=phrase,
            reply_markup=size_buttons(sizes),
        )
        user_sessions[chat_id] = {
            'name': product_name
        }

    if callback_query.data.startswith('product_size|'):
        product_size = callback_query.data.split('|')[1]
        chat_id = callback_query.message.chat.id
        phrase = f'Выбранный размер: {product_size}'
        await bot.send_message(
            chat_id=chat_id,
            text=phrase,
            reply_markup=sell_type_buttons()
        )
        user_sessions[chat_id] = {
            **user_sessions[chat_id],
            'size': product_size,
            }

    if callback_query.data.startswith('sell_type|'):
        sell_type = callback_query.data.split('|')[1]
        chat_id = callback_query.message.chat.id
        user_sessions[chat_id] = {
            **user_sessions[chat_id],
            'sell_type': sell_type,
        }
        user_session =  user_sessions[chat_id]
        number_check = await get_check_number(user_sessions[chat_id])
        phrase = f'🎈Вы добавили продажу💰\n Товар: {user_session["name"]}.\nНомер чека: {number_check}\n\nПроверьте таблицу📝'
        await bot.send_message(
            chat_id=chat_id,
            text=phrase,
        )
        


    await bot.send_message(
        chat_id=chat_id,
        text='Меню',
        reply_markup=menu_markup()
    )       


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
