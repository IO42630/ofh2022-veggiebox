
def replace(array: [], a, b):
    for x in range(0, len(array)):
        if array[x] == a:
            array[x] = b
    return array
