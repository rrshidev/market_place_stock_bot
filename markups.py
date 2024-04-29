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


def buy_sell_menu(product_name) -> InlineKeyboardMarkup:
    
    builder = InlineKeyboardMarkup()
    
    builder.row(
        InlineKeyboardButton(
            text='Новый чек',
            callback_data=f'new_check|{product_name}'
        )
        
    )
    builder.row(
        InlineKeyboardButton(
            text='Возврат товара',
            callback_data=f'money_back|{product_name}'
        )
    )
    return builder


def size_buttons(sizes) -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    for size in sizes:
        builder.row(
            InlineKeyboardButton(
                text=size,
                callback_data=f'category|{size}'
            )
        )
    return builder
