#!/usr/bin/python

samples = [
"""
0 -> IE,0R
E -> 0L
"""
,
"""
0 -> IE,0R
E -> 0L
"""
,
"""
0 -> 0L, 1E
E -> 0R
"""
,
"""
0 -> 1E, 0L
E -> 0R
"""
,

"""
0 -> 1E, 0R
E -> 0L
"""
,


"""
0 -> 0R, 1E
E -> 0L
"""
,

"""
0 -> 0L, 1R
1 -> 1L, 2E
E -> 0R
"""
,


"""
0 -> 0L, 1R
1 -> 2E, 1L 
E -> 0R
"""
,

"""
0 -> 0L, 1L
1 -> 1R, 2E
E -> 0R
""" 
,
# a3

"""
title a3
0 -> 0L, 1R
1 -> 1L, 2R
2 -> 2L, IE
E -> 0R
"""

,

# a4
"""
title a4
0 -> 0L, 1R
1 -> 1L, 2R
2 -> 2L, 3R
3 -> 3L, IE
E -> 0R
"""


,

# a5

"""
title a5
0 -> 0L, 1R
1 -> 1L, 2R
2 -> 2L, 3R
3 -> 3L, 4R
4 -> 4L, IE
E -> 0R
"""
,
# a6
"""
title a6
0 -> 0L, 1R
1 -> 1L, 2R
2 -> 2L, 3R
3 -> 3L, 4R
4 -> 4L, 5R
5 -> 5L, IE
E -> 0R
"""

,

# a2
"""
title a2
0 -> 0L, 1R
1 -> 1L, 2E
E -> 0R
"""
, 
# a
"""
title a
0 -> 0L, 1E
E -> 0R 
"""
,
# for andy
"""
0 -> IE, 0L
E -> 0R
"""
,

"""
0 -> 1L, 0R
1 -> IE, 1R
E -> 0L
"""
,

"""
0 -> 1L, 0R
1 -> 2L, 1R
2 -> IE, 2R
E -> 0L
"""
,

"""
0 -> 1L, 0R
1 -> 2L, 1R
2 -> 3L, 2R
3 -> IE, 3R
E -> 0L
"""
,
"""
0 -> IE, 0R
E -> 0L
"""

,
"""
0 -> 1L, 0R
1 -> IE, 1R
E -> 0L
"""

,
"""
0 -> 1L, 0R
1 -> 2L, 1R
2 -> IE, 2R
E -> 0L
"""
,
"""
0 -> 1L, 0R
1 -> 2L, 1R
2 -> 3L, 2R
3 -> IE, 3R
E -> 0L
"""

,
"""
0 -> IE, 1R
1 -> 1L, 0R
E -> 0L
"""

,
 #00222112102210000

"""
0 -> 2R, 0R
1 -> IE, 1R
2 -> 1L, 0L
E -> 2L
"""
,
 #00211002212000102
"""
0 -> 1L, 2L
1 -> IE, 1R
2 -> 0R, 2R
E -> 0L
"""
,

# 01110001122221222


"""
0 -> IE, 1L
1 -> 0R, 1R
E -> 0L
"""
,

# 02021022001121110

"""
0 -> 1R, 0R
1 -> IE, 0L
E -> 1L
"""
,
# 01110001122221222

"""
0 -> 0L, 0R
1 -> IE, 2L
2 -> 1R, 2R
E -> 1L
"""
,
#01110001122221222

"""
0 -> IE, 2L
1 -> 1L, 1R
2 -> 0R, 2R
E -> 0L
"""
,
"""
gold 01120011102221120
0 -> IE, 0L
E -> 0R
"""
,
"""
gold 12122221020010011
0 -> 0R,IE
E -> 0L
"""
,

]


import re



class ccompilegate:
    title = None
    gold = None
    allgates = {}
    def __init__(self, id, o1node, o1side, o2node, o2side):
        self.id = id

        if o1side == 'E':
            o1node = None

        self.o1node = o1node
        self.o1side = o1side
        self.o2node = o2node
        self.o2side = o2side
        self.external = False

        ccompilegate.allgates[ id ] = self

    @staticmethod
    def get_externalnode():
        return str(len(ccompilegate.allgates)-1)

    def update_other( self ):

        if self.id == 'E':
            self.external = True
            self.id = ccompilegate.get_externalnode()
            #print "Updating E node"
            ccompilegate.allgates[ self.id ] = self
            del ccompilegate.allgates[ 'E' ]
            ccompilegate.externalnode = self.id

        if self.o1side == "L":
            ccompilegate.allgates[ self.o1node ].input1node = self.id
            ccompilegate.allgates[ self.o1node ].input1side = 'L'
            if self.external:
                ccompilegate.allgates[ self.o1node ].input1side = 'R'

        if self.o1side == "R":
            ccompilegate.allgates[ self.o1node ].input2node = self.id
            ccompilegate.allgates[ self.o1node ].input2side = 'L'
            if self.external:
                ccompilegate.allgates[ self.o1node ].input2side = 'R'



        if self.o2side == "L":
            ccompilegate.allgates[ self.o2node ].input1node = self.id
            ccompilegate.allgates[ self.o2node ].input1side = 'R'
        if self.o2side == "R":
            ccompilegate.allgates[ self.o2node ].input2node = self.id
            ccompilegate.allgates[ self.o2node ].input2side = 'R'
            


        if self.o1side == "E":
            ee = ccompilegate.allgates[ ccompilegate.get_externalnode() ]
            ee.input1node = self.id
            ee.input1side = 'L'
            self.o1node = ccompilegate.get_externalnode()
            self.o1side = 'R'


        if self.o2side == "E":
            ee = ccompilegate.allgates[ ccompilegate.get_externalnode() ]
            ee.input1node = self.id
            ee.input1side = 'R'
            self.o2node = ccompilegate.get_externalnode()
            self.o2side = 'R'


    
def compile ( source ):
    ccompilegate.allgates = {}
    ccompilegate.title = None
    ccompilegate.gold = None

    x = source.split("\n")
    for inputs in x:
        if len(inputs)==0:
            continue
        if "title" in inputs.lower():
            ccompilegate.title = inputs
            continue
        if "gold" in inputs.lower():
            ccompilegate.title = inputs
            continue
        m = re.match(r"([\d]+)\s*->\s*([\dI]+)([ERL])\s*,\s*([I\d]+)([ERL])", inputs )
        if m:
            g = m.groups()
            #print g
            ccompilegate( g[0], g[1], g[2], g[3], g[4] )
        else:
            m = re.match(r"(E)\s*->\s*([\dI]+)([RL])", inputs )
            if m:
                g = m.groups()
                #print g
                ccompilegate( g[0], g[1], g[2], None, None )
            else:
                print inputs, "no match"
    

    c = ccompilegate
        
    
    c.allgates['E'].update_other()
    for i in c.allgates:
        c.allgates[i].update_other()
    
    
    keys = ccompilegate.allgates.keys()
    keys.sort()
    
    
    
    print "%sL:"%(c.get_externalnode())
    for j in keys:
        i = ccompilegate.allgates[j]
        if not i.external:
            print "%s%s%s%s0#%s%s%s%s,"%( i.input1node, i.input1side, i.input2node, i.input2side, i.o1node, i.o1side, i.o2node, i.o2side )
    
    i = c.allgates[ c.get_externalnode() ]
    print "X%s%s0#X%s%s:"%( i.input1node, i.input1side, i.o1node, i.o1side )
    
    
    print "%sL"%(c.get_externalnode())


import sys
if len(sys.argv) == 1:
    for code in samples:
        print "================="
        print code
        compile( code )
else:
    code = open( sys.argv[1], "rt" ).read()
    print "================="
    print code
    compile( code )



