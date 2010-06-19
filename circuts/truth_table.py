

truth = {
{ (0, 1), (0, 1) },

{ (1, 2), (1, 2) },

{ (0, 0), (0, 0) },

{ (2, 1), (2, 1) },

{ (1, 1), (1, 1) },

{ (2, 0), (2, 0) },

{ (2, 2), (2, 2) },

{ (1, 0), (1, 0) },

{ (0, 2), (0, 2) },

}

def generate_default_truth_table():
    tt = {}
    for i in xrange(3):
        for j in xrange( 3 ):
            tt[ (i,j) ] = (i,j)
    
    print "truth = {"
    for i in tt:
        print "{ %s, %s },\n"%( i, tt[i] )
    print "}"


# generate_default_truth_table()
