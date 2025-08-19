## 讀取檔案內容
f = open('note.txt', 'r')
file1 = f.readlines()
print(file1)
f.close()

## 寫入日記
import os # 引入 os 模組，用來處理檔案相關

filename = 'diary.txt'

# 檢查檔案是否存在
if os.path.exists(filename):
    print('檔案已存在，這會覆蓋原本的內容')

# 使用者輸入日記內容
content = input('請輸入一段文字：')

# 寫入檔案（覆蓋原本內容）
with open(filename, 'w', encoding = 'utf-8') as file:
    file.write(content)

print('日記已儲存到 diary.txt')
f.close

# 追加記帳紀錄
user_input = input('請輸入消費紀錄（格式：日期 項目 金額）')
f = open('expenses.txt', 'a')
f.write('\n'+user_input)
f.close()