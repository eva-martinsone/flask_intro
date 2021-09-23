FILE_NAME = "data.txt"

def pievienot(rindina):
    f = open(FILE_NAME, 'a', encoding="utf-8")
    f.write(rindina + '\n')
    f.close()

def lasitRindinas():
    with open(FILE_NAME, 'r', encoding="utf-8") as f:
        rindinas = f.readlines()

    return rindinas
    