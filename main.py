import openpyxl

import find
2

song_name = 0
song_alter = 0
row_count = 0
col_count = 0

print("Mode Select")
print("1 for add alter name")
print("2 for check alter name")
mode_select = input()

if mode_select == "2":
    print("key")
    print(find.song_find(input()))
