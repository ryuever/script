import os, sys, re

path  = sys.argv[1]
stext = sys.argv[2]

input_file = sys.stdin
output_file = sys.stdout

output_file = open(path+"/difference.txt",'w')
re_temp = ".*" + stext + ".*"
temp = re.compile(re_temp)

for filename in os.listdir(path):
    input_file = open(path+filename)
    # first_time is used to ensure you write the name of matched found file for only one times.
    first_time = True
    matched = False
    # count the line number
    count = 0
    for s in input_file:
        result = temp.match(s)
        count = count + 1
        if result :
            if first_time:
                output_file.write("File "+filename + " :\n")
            output_file.write(str(count) + s)
            # output_file.write(`count` + s)
            first_time = False
            matched = True
    if matched:
        output_file.write("\n")
output_file.close()
input_file.close()
