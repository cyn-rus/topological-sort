# to read file
def read_file(file_name):
    arr = []
    if file_name[-4:] != ".txt":
        file_name += ".txt"
    f = open("../test/"+file_name, 'r')
    for x in f:
        arr.append(x)
    return arr

# remove unnecessary symbols (commas and newline)
def remove_sym(arr):
    for i in range (len(arr)):
        arr[i] = arr[i].replace('.', '').replace('\n', '')

# convert to matrix
def convert_listception(arr):
    remove_sym(arr)
    new_arr = []
    for i in range (len(arr)):
        new_arr.append(arr[i].split(","))
        for j in range (1, len(new_arr[i])):
            new_arr[i][j] = new_arr[i][j].lstrip()
    return new_arr