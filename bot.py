import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("key.json", scopes=scope)
client = gspread.authorize(creds)

sheet = client.open("bot-test").sheet1

data = sheet.get_all_records()

print("讀到資料：")
print(data)
