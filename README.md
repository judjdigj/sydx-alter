# A tool to add/find alternative name of song for Ricebot
## This project is still work in progress
W.I.P.
## Feature
A shorter form "song_alter_test" was created for testing.
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
You need two arguement for adding new alternative name.  
One for the new alternative name need to be added, and the other is the existed name, which can can alternative name or original name.
```
alter_add(new_alternative_name, old_original_or_alter_name)
```
### Comment on the alternative name contributor
All the alternative name will be related with the contributor's ID.
```
W.I.P.
```
## Acknowledgement
[Ricebot](https://github.com/FreezeRasis/Ricebot-Nonebot)  
[Openpyxl](https://openpyxl.readthedocs.io/en/stable/)  
[SQLite](https://sqlite.org/)  