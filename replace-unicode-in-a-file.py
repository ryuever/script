import os, sys

nargs = len(sys.argv)
if not 3 <= nargs <= 5:
    print "usage: %s search_text replace_text [infile [outfile]]" % \
        os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    # print type(stext)
    # temp = stext.decode("unicode-escape")
    input_file = sys.stdin
    output_file = sys.stdout
    if nargs > 3:
        input_file = open(sys.argv[3])
    if nargs > 4:
        output_file = open(sys.argv[4], 'w')
    for s in input_file:
        # output_file.write(s.decode("utf-8").replace(u"\u00a0", "").encode("utf-8"))
        output_file.write(s.decode("utf-8").replace(stext.decode("unicode-escape"), rtext).encode("utf-8"))
    # print temp
    # print type(temp)
    output_file.close( )
    input_file.close( )
