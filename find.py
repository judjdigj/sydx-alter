import openpyxl

book = openpyxl.load_workbook('song_alter_test.xlsx')
sheet = book.active

def song_find(key):
    row_count = 0
    O = 0
    for row in sheet.iter_rows():
        row_count = row_count + 1
        for cell in row:
            if cell.value == key:
                return sheet.cell(row_count, 1).value
            elif cell.value == None:
                break
    return "no found"