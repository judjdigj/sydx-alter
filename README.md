# A tool to add/find alternative name of song for Ricebot
## Introduction
Based on [Openpyxl](https://openpyxl.readthedocs.io/en/stable/), This project is a dictionary to find/record the alternative name for a song.  
Designed for [Ricebot](https://github.com/FreezeRasis/Ricebot-Nonebot), but can be used for other bot.
## Usage
A shorter form "song_alter_test" was created for testing. In actual usage, you need to change the form to the full one.  
In tools.py
```
book = openpyxl.load_workbook('song_alter_test.xlsx')
```
To
```
book = openpyxl.load_workbook('song_alter.xlsx')
```
### Find song with alternative name
You need one arguement, which is the keyword of the alternative name.
```
find_song(keyword)
```
When input the alternative name:
```
albida
```
You will get the original name:
```
ALBIDA Powerless Mix
```
### Add alternative name for song
You need 3 arguement for adding new alternative name.  
One for the new alternative name need to be added.  
One for the existed name, which can be the existed alternative name or original name.  
One for the QQID, which can be got by Ricebot
```
alter_add(new_alternative_name, old_original_or_alter_name, QQID)
```
### Show all the alternative name of a song.
W.I.P.
## Acknowledgement
[Ricebot](https://github.com/FreezeRasis/Ricebot-Nonebot)  
[Openpyxl](https://openpyxl.readthedocs.io/en/stable/)  