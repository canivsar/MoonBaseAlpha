#!/usr/bin/python 

#print out roman numbers from 1 1000 - no zero required


def pattern( pat ):
    one, five, ten = list( pat )
    yield one
    yield one * 2 
    yield one * 3
    yield one + five
    yield five
    yield five + one
    yield five +  one * 2 
    yield five +  one * 3
    yield one + ten


#patlist = [ "IVX" , "XLC", "CDM" ]




for m in xrange(4):
        ms = 'M'*m
        print ms

	for i in pattern( "IVX" ):
	    print  i
	
	for j in pattern( "XLC" ):
	    print j
	    for i in pattern( "IVX" ):
	        print  j+i
	
	for k in pattern( "CDM" ):
            mk = ms + k
	    print mk
	
	    for i in pattern( "IVX" ):
	        print  mk + i
	
	    for j in pattern( "XLC" ):
                mj = mk + j
	        print mj
	        for i in pattern( "IVX" ):
	            print  mj +i
	

