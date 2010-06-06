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

def PrefixPattern( prefix, pat ):
    for i in pattern( pat ):
        yield prefix + i
        
for T in xrange(4):
    for M in PrefixPattern( 'M'*T, "CDM" ):
        for C in PrefixPattern( M, "XLC" ):
            for I in PrefixPattern( C, "IVX" ):
                print  I

        
