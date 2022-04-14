#This main.py is only served as testing.
import tools

while True:
    print("Mode Select")
    print("1 for add alter name")
    print("2 for check alter name")
    mode_select = input()

    if mode_select == "1":
        print("new alter")
        new = input()
        print("old name")
        old = input()
        print("qqid")
        qqid = input()
        print(tools.alter_add(new, old, qqid))

    if mode_select == "2":
        print("key")
        print(tools.song_find(input()))
