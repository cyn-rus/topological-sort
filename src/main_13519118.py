from setup_13519118 import read_file, remove_sym, convert_listception
from process_13519118 import remove_preq, find_no_preq, taken_all
from out_13519118 import print_sem

file = input("Masukkan nama file: ")
kuliah = read_file(file)
kuliah = convert_listception(kuliah)
semester = []

# loop di bawah ini merupakan tahapan decrease
for i in range (len(kuliah)):
    no_preq = []
    find_no_preq(kuliah, no_preq)
    semester.append(no_preq)
    remove_preq(kuliah, no_preq)
    if taken_all(kuliah):
        break
print_sem(semester)