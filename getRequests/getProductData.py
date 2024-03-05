from getRequests.getRequest import get_service
from Secrets.config import sheet_id


def get_product_data(product_index):

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
    print(product_name)
   
    product_message = ''
    cnt = 0
    for product in product_names:
        if product == product_name:
            product_message += f'{product_name} - остаток: {product_balance[cnt]} - разымер: {product_size[cnt]}\n'
        cnt += 1
    return product_message