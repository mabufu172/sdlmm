def checkForGameInfo():
    with open("gameinfoexample.txt", "r") as file:
        line = file.read()
        print(line)
    return True