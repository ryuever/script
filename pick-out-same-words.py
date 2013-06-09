import re
import sys

path_1 = sys.argv[1]
path_2 = sys.argv[2]

file_input1 = open(path_1)
file_input2 = open(path_2)
file_difference = open('file_difference.txt', 'w')
file_same = open('file_same.txt', 'w')

list_temp1 = file_input1.read()
list_temp2 = file_input2.read()

list_input1 = re.split("\W+", list_temp1)
list_input2 = re.split("\W+", list_temp2)

difference_temp = []
same_temp = []
len_input2 = len(list_input2)
len_input1 = len(list_input1)


def word_to_list(wd, list_temp):
    for i in list_temp:
        if wd is i:
            return True
    return False

if len_input1 < len_input2:
    for word in list_input1:
        identifier = word_to_list(word, list_input2)
        if identifier:
            same_temp.append(word)
        else:
            difference_temp.append(word)
else:
    for word in list_input2:
        # print "words:", word
        # print "list: ", list_input2
        identifier = word_to_list(word, list_input1)
        if identifier:
            same_temp.append(word)
        else:
            difference_temp.append(word)
            # print same_temp
same_string = "\n".join(same_temp)
difference_temp = "\n".join(difference_temp)

file_same.write(same_string)
file_difference.write(difference_temp)

file_same.close()
file_difference.close()
file_input1.close()
file_input2.close()
