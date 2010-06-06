#!/usr/bin/python 

#print out roman numbers from 1 3999 - no zero required
#patlist = [ "IVX" , "XLC", "CDM" ]

def pattern( pat ):
    I, V, X = list( pat )
    yield ''
    yield I
    yield I + I 
    yield I + I + I
    yield I + V
    yield V
    yield V + I
    yield V + I + I
    yield V + I + I + I
    yield I + X

def pattern_with_prefix( prefix, pat ):
    for i in pattern( pat ):
        yield prefix + i
        
def one_to_a_thousand( prefix ):
    for j in pattern_with_prefix( prefix, "XLC" ):
        for i in pattern_with_prefix( j, "IVX" ):
            print  i
    
for m in xrange(4):
    for k in pattern_with_prefix( 'M'*m, "CDM" ):
        one_to_a_thousand( k )
        
