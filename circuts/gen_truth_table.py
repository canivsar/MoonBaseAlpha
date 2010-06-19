

import truth_table

def generate_default_truth_table():
    tt = {}
    for i in xrange(3):
        for j in xrange( 3 ):
            tt[ (j,i) ] = list(( 0,0 ) )
    
    print "truth = {"
    comma = " "
    kk = tt.keys()
    kk.sort()
    for i in kk:
        print "%s %s : %s"%( comma, i, tt[i] )
        comma = ","
    print "}"


generate_default_truth_table()
