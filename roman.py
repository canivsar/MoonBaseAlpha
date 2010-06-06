#!/usr/bin/python 

#print out roman numbers from 1 3999 - no zero required

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

# ---------------------------------------        
# Simple case of 3.3 patterns

def PrefixPattern( prefix, pat ):
    for i in pattern( pat ):
        yield prefix + i
        
for T in xrange(4):
    for M in PrefixPattern( 'M'*T, "CDM" ):
        for C in PrefixPattern( M, "XLC" ):
            for I in PrefixPattern( C, "IVX" ):
                print  I

# ---------------------------------------        
# Extra Credit 
# General case that can handle N patterns
def PrefixPattern2( prefix, patlist ):
    for i in pattern( patlist[0] ):
        if len( patlist ) == 1:
            yield prefix + i
        else:
            for j in PrefixPattern2( prefix + i, patlist[1:] ):
                yield j

def Call_PrefixPattern2_Thrice():
    Patlist = [ "CDM" , "XLC", "IVX"   ]
    for T in xrange(4):
        for i in PrefixPattern2( 'M'*T, Patlist ):
            print i
    
        
