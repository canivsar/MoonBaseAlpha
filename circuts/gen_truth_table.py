
truth = {
  (0, 1) : [0, 0]
, (1, 2) : [0, 0]
, (0, 0) : [0, 0]
, (2, 1) : [0, 0]
, (0, 2) : [0, 0]
, (2, 0) : [0, 0]
, (2, 2) : [0, 0]
, (1, 0) : [0, 0]
, (1, 1) : [0, 0]
}


def generate_default_truth_table():
    tt = {}
    for i in xrange(3):
        for j in xrange( 3 ):
            tt[ (j,i) ] = list(( 0,0 ) )
    
    print "truth = {"
    comma = " "
    for i in tt:
        print "%s %s : %s"%( comma, i, tt[i] )
        comma = ","
    print "}"


generate_default_truth_table()
