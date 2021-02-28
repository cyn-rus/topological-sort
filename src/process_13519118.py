# remove substring
# arr: list of all nodes
# preq: list of nodes that need to be removed in arr
def remove_preq(arr, preq):
    for i in range (len(preq)):
        for j in range (len(arr)):
            if preq[i] in arr[j]:
                arr[j].remove(preq[i])

# to find which one has no prerequisite (tahapan decrease)
# arr: list of all nodes
# no_preq: list of nodes that need to be removed in arr
def find_no_preq(arr, no_preq):
    if len(arr) == 0:
        return
    else:
        if len(arr[0]) == 1:
            no_preq.extend(arr[0])
        find_no_preq(arr[1:], no_preq)

# to check whether all of the values are taken already
# arr: list of all nodes
def taken_all(arr):
    for i in range (len(arr)):
        if len(arr[i]) != 0:
            return False
    return True