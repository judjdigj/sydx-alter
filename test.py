from openpyxl import Workbook
import sqlite3

book = Workbook()
sheet = book.active

conn = sqlite3.connect('myDB.sqlite3')
cursor = conn.cursor()
cursor.execute('select name from diffinfo')
value = cursor.fetchall()

rows = value

for row in rows:
    sheet.append(row)

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=6, max_col=3):
    for cell in row:
        print(cell.value, end=" ")
    print()    

book.save('song_alter.xlsx')