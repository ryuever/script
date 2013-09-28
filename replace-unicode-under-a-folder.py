import os, sys

nargs = len(sys.argv)
if not 3 <= nargs <= 5:
    print "usage: %s search_text replace_text [infile [outfile]]" % \
        os.path.basename(sys.argv[0])
else:
    path  = sys.argv[1]
    stext = sys.argv[2]
    rtext = sys.argv[3]

    # iterate files under folder path.
    for filename in os.listdir(path):
        input_file = open(path+filename)

        # create a new folder under current directory to store these replaced file.
        d = path + "replaced/"
        if not os.path.exists(d):
            os.mkdir(d)
        output_file = open(d + filename,'w')

        for s in input_file:
            # output_file.write(s.decode("utf-8").replace(stext.decode("unicode-escape"), rtext).encode("utf-8"))
            output_file.write(s.decode("utf-8").replace(stext.decode("unicode-escape"), rtext))
        output_file.close( )
        input_file.close( )
