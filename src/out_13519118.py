from romanDict_13519118 import roman

# to print
def print_sem(arr):
    for i in range (len(arr)):
        print('Semester', roman[i+1], ': ', end ='')
        for j in range (len(arr[i])):
            print(arr[i][j], end='')
            if j < len(arr[i])-1:
                print(', ', end='')

        if i == len(arr)-1:
            print('.', end='')
        print()