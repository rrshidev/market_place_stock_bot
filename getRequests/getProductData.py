import os

from getRequests.getRequest import get_service
from Secrets.config import sheet_id, path_to_photos


async def get_product_data(product_index, flag):

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

    files_list = os.listdir(path_to_photos)
    photo_name = product_name + '.jpg'
    if photo_name in files_list:
        flag = True
    product_list.append(product_message)
    product_list.append(flag)
    product_list.append(photo_name)
    return product_list