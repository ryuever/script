import os
import sys

path = sys.argv[1]
suffix = sys.argv[2]

for filename in os.listdir(path):
    base = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    filename_new = path + '/' + base + suffix + extension
    os.rename(path + '/' + filename, filename_new)
