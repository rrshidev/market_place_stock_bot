from Secrets.config import sheet_id
from getRequests.getRequest import get_service

async def get_sizes(product_name):
    print('product----->', product_name)
    get_sheet_name = 'Склад'
    values_product_data = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{get_sheet_name}!A3:K',
        majorDimension='COLUMNS'
        # majorDimension='ROWS'
    ).execute()
   
    stock_data = values_product_data['values']
    size_list = []
    cnt = 0
    for name in stock_data[1]:
        if name == product_name:
            size_list.append(stock_data[4][cnt])
        cnt += 1
    return size_list
    print('size_list--->', size_list)

