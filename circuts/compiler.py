
source = """0 -> IE,0R
E -> 0L"""

import re

class ccompilegate:
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
            print "Updating E node"
            ccompilegate.allgates[ self.id ] = self
            del ccompilegate.allgates[ 'E' ]
            ccompilegate.externalnode = self.id

        if self.o1side == "L":
            ccompilegate.allgates[ self.o1node ].input1node = self.id
            ccompilegate.allgates[ self.o1node ].input1side = 'L'
        if self.o1side == "R":
            ccompilegate.allgates[ self.o1node ].input2node = self.id
            ccompilegate.allgates[ self.o1node ].input2side = 'L'

        if self.external:
            ccompilegate.allgates[ self.o1node ].input1side = 'R'


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


    

x = source.split("\n")
for inputs in x:
    m = re.match(r"([\d]+)\s*->\s*([\dI]+)([ERL]),([\d]+)([ERL])", inputs )
    if m:
        g = m.groups()
        print g
        ccompilegate( g[0], g[1], g[2], g[3], g[4] )
    else:
        m = re.match(r"(E)\s*->\s*([\dI]+)([RL])", inputs )
        if m:
            g = m.groups()
            print g
            ccompilegate( g[0], g[1], g[2], None, None )
        else:
            print inputs, "no match"

c = ccompilegate
    

c.allgates['E'].update_other()
for i in c.allgates:
    print "Updating ",i, c.allgates[i].id
    c.allgates[i].update_other()


keys = ccompilegate.allgates.keys()
keys.sort()
print keys


print "%sL:"%(c.get_externalnode())
for j in keys:
    i = ccompilegate.allgates[j]
    if not i.external:
        print "%s:%s%s%s%s0#%s%s%s%s,"%(i.id, i.input1node, i.input1side, i.input2node, i.input2side, i.o1node, i.o1side, i.o2node, i.o2side )

i = c.allgates[ c.get_externalnode() ]
print "%s:X%s%s0#X%s%s:"%(i.id, i.input1node, i.input1side, i.o1node, i.o1side )


print "%sL"%(c.get_externalnode())
