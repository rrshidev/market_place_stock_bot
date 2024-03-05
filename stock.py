from getRequests.getRequest import get_service
from Secrets.config import sheet_id

spreadsheet_id = sheet_id

async def get_stock():
    sheet_name = 'Склад'
    values = get_service().spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!A:E',
        majorDimension='ROWS'
    ).execute()
    tableData = values['values']
    # print(tableData)

    return tableData