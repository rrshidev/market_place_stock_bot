from getRequests.getRequest import get_service
from Secrets.config import sheet_id

async def get_categories():

    sheet_name = 'Склад'
    values = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!G3:G',
        majorDimension='COLUMNS'
        # majorDimension='ROWS'
    ).execute()
    tableData = values['values']
    tableData = tableData[0]
    sortTable = []
    for category in tableData:
        if category not in sortTable:
            sortTable.append(category)
    sortTable.sort()
    # print('SORTED--->', sortTable)
    return sortTable