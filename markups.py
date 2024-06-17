from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from services.getCodingCallback import generate_callback_data


def menu_markup() -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    builder.row(
        InlineKeyboardButton(
            text="Показать остаток по всему складу", 
            callback_data='nc|Ремень Louis Vuitton Monogram (Графитовый)'
        )
    )

    builder.row(
        InlineKeyboardButton(
            text="Быстрая продажа по артикулу", 
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

    builder.row(
        InlineKeyboardButton(
            text=name,
            callback_data=f'product|{index}'
        )
    )

    return builder


def buy_sell_menu(product_index) -> InlineKeyboardMarkup:
    
    builder = InlineKeyboardMarkup()
    
    builder.row(
        InlineKeyboardButton(
            text='Новый чек',
            callback_data=f'new_check|{product_index}'
        )
    )

    builder.row(
        InlineKeyboardButton(
            text='Возврат товара',
            callback_data=f'money_back|{product_index}'
        )
    )

    return builder


def size_buttons(sizes) -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    for size in sizes:
        builder.row(
            InlineKeyboardButton(
                text=size,
                callback_data=f'product_size|{size}'
            )
        )

    return builder


def sell_type_buttons() -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    builder.row(
        InlineKeyboardButton(
            text='Оффлайн',
            callback_data='sell_type|offline'
        )
    )
    
    builder.row(
        InlineKeyboardButton(
            text='Доставка',
            callback_data='sell_type|delivery'
        )
    )

    return builder


def status_buttons() -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    builder.row(
        InlineKeyboardButton(
            text='Бронь',
            callback_data='status|Бронь'
        )
    )

    builder.row(
        InlineKeyboardButton(
            text='В пути',
            callback_data='status|В пути'
        )
    )

    builder.row(
        InlineKeyboardButton(
            text='Успешно',
            callback_data='status|Успешно'
        )
    )
    
    return builder


def check_table_markup() -> InlineKeyboardMarkup:

    builder = InlineKeyboardMarkup()

    builder.row(
        InlineKeyboardButton(
            text='Проверить таблицу',
            url='https://docs.google.com/spreadsheets/d/1gxl-vr7RuF2SRuXVlifO4tIzWeYJBHUM_XZWjCz7q7o/edit#gid=1680109685'
        )
    )
