import gspread
from google.oauth2.service_account import Credentials

# 連線 Google API
creds = Credentials.from_service_account_file("key.json")
client = gspread.authorize(creds)

# 開啟 Sheet（名字要完全一樣）
sheet = client.open("你的Google Sheet名稱").sheet1

# 讀取資料
data = sheet.get_all_records()

print("Sheet data:")
print(data)
