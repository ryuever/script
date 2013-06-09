import glob
import sys

mydir = sys.argv[1]

for f in glob.iglob(os.listdir(my_dir), "*.tx?"):
    print f
