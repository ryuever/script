import os
import re
import sys

path = sys.argv[1]
older_word = sys.argv[2]
new_word = sys.argv[3]

for filename in os.listdir(path):
    print "filename : ", filename
    filename_new = re.sub(older_word, new_word, filename)
    print path+filename_new
    print path+filename
    os.rename(path+"/"+filename, path+"/"+filename_new)
