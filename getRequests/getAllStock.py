from getRequests.getRequest import get_service
from Secrets.config import sheet_id
 

async def get_stock():
    
    sheet_name = 'Склад'
    values = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!A:E',
        # majorDimension='COLUMNS'
        majorDimension='ROWS'
    ).execute()
    tableData = values['values']

    return tableData
d