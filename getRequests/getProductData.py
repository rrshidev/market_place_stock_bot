import os

from getRequests.getRequest import get_service
from Secrets.config import sheet_id, path_to_photos


async def get_product_data(product_index, flag):
    print('FLAG---->', flag)
    sheet_name = 'Склад'
    
    values_product_data = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!B3:E',
        majorDimension='COLUMNS'
        # majorDimension='ROWS'
    ).execute()
   
    tableData = values_product_data['values']
   
    product_names = tableData[0]
    product_balance = tableData[1]
    product_size = tableData[3]
    product_name = product_names[int(product_index)]
    product_message = ''
    product_list = []
    cnt = 0
    for product in product_names:
        if product == product_name:
            product_message += f'{product_name} - остаток: {product_balance[cnt]} - размер: {product_size[cnt]}\n'
        cnt += 1
    product_list.append(product_message)
    files_list = os.listdir(path_to_photos)
    if product_name + '.jpg' in files_list:
        flag = True
        photo_name = product_name + '.jpg'
        product_list.append(flag)
        product_list.append(photo_name)
        print('FLAG111---->', flag)
        print('ИМЯ ПРОДАКТА--->',product_name)
        return product_list
    else:
        product_list.append(flag)
        print('FLAG111---->', flag)
        return product_list