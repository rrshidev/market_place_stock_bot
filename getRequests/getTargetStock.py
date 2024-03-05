from getRequests.getRequest import get_service
from Secrets.config import sheet_id


async def get_names_of_product(category):

    sheet_name = 'Склад'
    
    values_names = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!B3:B',
        majorDimension='COLUMNS'
        # majorDimension='ROWS'
    ).execute()
    tableData1 = values_names['values']
    tableNames = tableData1[0]
   
    sortTable = []

    values_categories = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{sheet_name}!G3:G',
        majorDimension='COLUMNS'
    ).execute()
    tableData2 = values_categories['values']
    tableCategories = tableData2[0]
    
    nameList = []
    indexLisst = []
    globalList = []
    cnt = 0
    for c in tableCategories:
        # print(c,tableCategories[cnt], cnt)
        if c == category and tableNames[cnt] not in nameList:
            index = cnt
            indexLisst.append(index)
            print('INDEX--->', cnt)
            nameList.append(tableNames[cnt])
            print('NAME--->', nameList)
        cnt += 1
   
    globalList.append(nameList)
    globalList.append(indexLisst)
    print('GLOBAL--->', globalList)
    # nameList.sort()

    return globalList