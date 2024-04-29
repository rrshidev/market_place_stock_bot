from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.getCodingCallback import generate_callback_data


def menu_markup() -> InlineKeyboardMarkup:
    builder = InlineKeyboardMarkup()

    builder.row(
        InlineKeyboardButton(
            text="Показать остаток по всему складу склад", 
            callback_data='check_balance'
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="Продажа", 
            callback_data='sell'
        )
    )
    builder.row(
        InlineKeyboardButton(
            text="Проверить остаток конкретного товара",
            callback_data='check_balance_product'
        )
    )
    return builder


def menu_markup_product(category) -> InlineKeyboardMarkup:
    print(type(category), category)
    builder = InlineKeyboardMarkup()
    for i in category:
        builder.row(
            InlineKeyboardButton(
                text=i,
                callback_data=f'category|{i}'
            )
        )
    return builder


def menu_markup_names_of_products(name, index) -> InlineKeyboardMarkup:
    builder = InlineKeyboardMarkup()
    # for name in names:
    # encode_name = generate_callback_data(name)
    builder.row(
        InlineKeyboardButton(
            text=name,
            callback_data=f'product|{index}'
        )
    )
    return builder


def buy_sell_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardMarkup()
    builder.row(
        InlineKeyboardButton(
            text='Новый чек',
            callback_data='new_check'

        )
        
    )
    builder.row(
        InlineKeyboardButton(
            text='Возврат товара',
            callback_data='money_back'
        )
    
    )
    return builder 
