#in this file is private function

def major_jp(word):
    for i in range(len(MAJOR_CHOICE)):
        if MAJOR_CHOICE[i][0] == word:
            rword = MAJOR_CHOICE[i][1]
    return rword

def place_jp(word):
    for i in range(len(PLACE_CHOISE)):
        if PLACE_CHOISE[i][0] == word:
            rword = PLACE_CHOISE[i][1]
    return rword
