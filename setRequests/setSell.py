from Secrets.config import sheet_id
from getRequests.getRequest import get_service

async def set_sell():

    sheet_name = 'P&L'
    values = get_service().spreadsheets().values().batchUpdate(
       
        spreadsheetId=sheet_id,
        
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"'{sheet_name}'!W3:X4",
                 "majorDimension": "ROWS",
                 "values": [["This is W3", "This is X3"], ["This is W4", "This is X4"]]},
                {"range": f"'{sheet_name}'!Y5:Z6",
                 "majorDimension": "COLUMNS",
                 "values": [["This is Y5", "This is Z6"], ["This is Y5", "=5+5"]]}
            ]
        }

    ).execute()