#!/usr/bin/python

circuit19 = """19L:
12R13R0#1R12R,
14R0L0#4R9L,
9R10R0#3L8L,
2L17R0#5L9R,
15R1L0#10R13R,
3L18R0#6L15L,
5L11R0#13L12L,
19R16R0#11R8R,
2R7R0#11L10L,
1R3R0#18L2L,
8R4L0#16L2R,
8L7L0#15R6R,
6R0R0#14L0L,
6L4R0#14R0R,
12L13L0#17L1L,
5R11L0#16R4L,
10L15L0#17R7R,
14L16L0#18R3R,
9L17L0#19R5R,
X18L0#X7L:
19L"""

import re
from truth_table import truth

#print circut.split(":")
    # inputs,outputs = gate.split("0#")
    # m = re.match("([\d])+([RL])([\d]+)([RL])", inputs )
    # if m:
    #     print gate,inputs, m.groups()
    # else:
    #     print gate,inputs, "no match"



class cgate:
    all = []
    count = 0
    def __init__(self, text, grps ):
        self.text = text
        self.groups = grps
        self.id = cgate.count
        if 'X' in text:
            self.i1node, self.i1side = grps[0], grps[1]
            self.i2node, self.i2side = None, None
            self.o1node, self.o1side = grps[2], grps[3]
            self.o2node, self.o2side = None, None
        else:
            self.i1node, self.i1side = grps[0], grps[1]
            self.i2node, self.i2side = grps[2], grps[3]
            self.o1node, self.o1side = grps[4], grps[5]
            self.o2node, self.o2side = grps[6], grps[7]

        cgate.count +=  1
        cgate.all.append( self )
    def is_external(self):
        return len( self.groups ) < 5
    def is_internal(self):
        x = len( self.groups ) > 5
        return x
    
    def update_links(self):
        if self.is_internal():
            self.o1 = int ( self.groups[4] )
        else:
            self.o1 = int ( self.groups[2] )
            
        self.o1s_input_label = cgate.all[ self.o1 ].input_label(self.id)

        if self.is_internal():
            self.o2 = int ( self.groups[6] )
            self.o2s_input_label = cgate.all[ self.o2 ].input_label(self.id)
        else:
            self.o2 = None
            self.o2s_input_label = None
            
    def input_label(self, id):
        if int(self.groups[0]) == id:
            return "i1"+self.groups[1]
        if self.is_external():
            raise "bad connection 1"
        if int(self.groups[2]) == id:
            return "i2"+self.groups[3]
        print "bad connection from ",self.id, id
        raise Exception("bad connection 2")

    def output_val( self, side ):
        if side == 'L':
            return self.o1
        if side == 'R':
            return self.o2
        raise "failure!"

        
def decode( circut ):

    print "digraph G {"

    circut = "".join( circut.split() )
    middle = circut.split(":")[1]
    for gate in middle.split(","):
        m = re.match(r"([\d]+)([RL])([\d]+)([RL])0#([\d]+)([RL])([\d]+)([RL])", gate )
        if m:
            x = cgate( gate, m.groups() )
            print "# %d %20s"%(x.id,gate), m.groups()
        else:
            m = re.match("X([\d]+)([RL])0#X([\d]+)([RL])", gate )
            if m:
                cgate( gate, m.groups() )
                print "# %20s"%gate, m.groups()
            else:
                print "# %20s"%gate, "no match"

    for g in  cgate.all :
        g.update_links()
        if g.is_external():
            print "# External Gate", g.text, g.groups
            print 'g%d [label="External g%d", shape=square ];'%(g.id, g.id )
            print 'g%d -> g%s [label="I1 %s", color=green ];'%(g.id, g.groups[0], g.groups[1] )
            print 'g%d -> g%s [label="o1 %s - %s"];'%(g.id, g.groups[2], g.groups[3], g.o1s_input_label )
        else:
            print "#", g.text, g.groups, g.i1node+ g.i1side,g.i2node+ g.i2side,g.o1node+ g.o1side,g.o2node+g.o2side
            #print 'g%d -> g%s [label="I1 %s", color=green];'%(g.id, g.groups[0], g.groups[1] )
            #print 'g%d -> g%s [label="I2 %s", color=green];'%(g.id, g.groups[2], g.groups[3] )
            print 'g%d -> g%s [label="o1 %s - %s"];'%(g.id, g.groups[4], g.groups[5], g.o1s_input_label )
            print 'g%d -> g%s [label="o2 %s - %s"];'%(g.id, g.groups[6], g.groups[7], g.o2s_input_label )

    print "}"


def process_input( inputbits ):
    print inputbits
    inputbits = [str(i) for i in inputbits]
    e = cgate.all[-1]
    e_o1 = cgate.all[ int( e.i1node ) ]

    for n in cgate.all:
        n.o1 = 0
        n.o2 = 0

    result = []
    for bit in inputbits:
        e.o1 = bit
        for n in cgate.all[:-1]: # last node is external - handle as special case
            i1 = cgate.all[ int(n.i1node) ].output_val( n.i1side )
            i2 = cgate.all[ int(n.i2node) ].output_val( n.i2side )
            n.o1, n.o2 = truth[ (i1,i2 ) ]


        result.append( e_o1.output_val( e.i1side ) )
        print result


decode( circuit19 )

input19 = [0,2,2,2,2,2,2,0,2,1,0,1,1,0,0,1,1]
process_input( input19 )


