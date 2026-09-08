import os

def exec():
    os.system("cls")
    print(r"""
 ___________ _     ___  ______  ___
/  ___|  _  \ |    |  \/  ||  \/  |
\ `--.| | | | |    | .  . || .  . |
 `--. \ | | | |    | |\/| || |\/| |
/\__/ / |/ /| |____| |  | || |  | |
\____/|___/ \_____/\_|  |_/\_|  |_/
          
 [  Simple Deadlock Mod Manager  ]
""")
    
    userinput = input("(1) Mod Menu\n(2) Check for gameinfo.gi\n(3) Configuration\n(4) Exit\n\nInput:\t")

    try:
        int(userinput)
    except:
        return exec()

    userinput = int(userinput)
    if userinput > 0 and userinput < 5:
        match userinput:
            case 1:
                print("Opens mod menu")
            case 2:
                print("Checks for gameinfo.gi")
            case 3:
                print("Opens config")
            case 4:
                os.system("cls")
                exit()
    else:
        return exec()