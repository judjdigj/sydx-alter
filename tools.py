import openpyxl

book = openpyxl.load_workbook('song_alter_test.xlsx') #Form contain song's original and alternative name. There's only one in the project.
sheet = book.active

def song_find(key):
    #You only need one arguement, which is the keyword of the song's alternative/original name 
    row_count = 0
    O = 0
    for row in sheet.iter_rows():
        row_count = row_count + 1
        for cell in row:
            if cell.value == key:
                return sheet.cell(row_count, 1).value   #Retuen the original name, which in the first column.
            elif cell.value == None:
                break
    return "song no found" #You can change to whatever you want for the bot.

def alter_add(new, exist):
    exist = song_find(exist)
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value == exist:
                for cell in row:
                    if sheet.cell(cell.row, cell.column+1).value == None:
                        sheet.cell(cell.row, cell.column+1).value = new
                        book.save('song_alter_test.xlsx')
                        return 'added'     #add alternative name
                    elif sheet.cell(cell.row, cell.column+1).value == new:
                        return "already in library"   #Check for existing alternative name
            elif cell.value == None:
                break
    return 'song no found'   #when no song found