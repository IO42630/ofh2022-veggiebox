for x in range(1, 51):

    f = open("./data/xlsx-rows/xl/kw" + str(x) + ".txt", "r")
    lines = f.readlines()

    result = ""
    for line in lines:
        line = line.replace('\n', '')

        if (line == ""):
            line = '0'
        result = result + '"' + line + '",'

    print("kw" + str(x) + " : " + result)
    br = 0
