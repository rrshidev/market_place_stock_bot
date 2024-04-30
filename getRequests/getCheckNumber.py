from Secrets.config import sheet_id
from getRequests.getRequest import get_service


async def get_check_number(user_sessions):
    
    session = user_sessions
    name, size, sell_type = session['name'], session['size'], session['sell_type']
    get_sheet_name = 'P&L'
    sells_data = get_service().spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=f'{get_sheet_name}!A10:D',
        majorDimension='COLUMNS'
        # majorDimension='ROWS'
    ).execute()
   
    checks_data = sells_data['values']
    check_list = [int(check) for check in checks_data[3]]
    current_check = str(max(check_list) + 1)

    set_index = str(len(check_list) + 10)
    number_list = [int(number) for number in checks_data[0]]
    current_number = str(max(number_list) + 1)
    print('current_number--->', current_number)
   
    values = get_service().spreadsheets().values().batchUpdate(
       
        spreadsheetId=sheet_id,
        
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"'{get_sheet_name}'!A{set_index}",
                 "majorDimension": "ROWS",
                 "values": [[f"{current_number}"]]},
                 {"range": f"'{get_sheet_name}'!B{set_index}",
                 "majorDimension": "ROWS",
                 "values": [[f"{name}"]]},
                 {"range": f"'{get_sheet_name}'!F{set_index}",
                 "majorDimension": "ROWS",
                 "values": [[f"{size}"]]},
                 {"range": f"'{get_sheet_name}'!J{set_index}",
                 "majorDimension": "ROWS",
                 "values": [[f"{sell_type}"]]},
                 {"range": f"'{get_sheet_name}'!D{set_index}",
                 "majorDimension": "ROWS",
                 "values": [[f"{current_check}"]]},
            ]
            ]
        }

    ).execute()

    return current_check