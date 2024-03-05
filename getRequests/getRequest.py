import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import httplib2


CREDENTIALS_FILE = './Secrets/sergio-mpb.json'


def get_credentials():

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive']
     )
    return credentials


def get_service():

    httpAuth = get_credentials().authorize(httplib2.Http())
    service = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth)
    return service