circut = """19L:
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
circut = "".join( circut.split() )
#print circut.split(":")
    # inputs,outputs = gate.split("0#")
    # m = re.match("([\d])+([RL])([\d]+)([RL])", inputs )
    # if m:
    #     print gate,inputs, m.groups()
    # else:
    #     print gate,inputs, "no match"


print "digraph G {"

class cgate:
    all = []
    count = 0
    def __init__(self, text, grps ):
        self.text = text
        self.groups = grps
        self.id = cgate.count
        cgate.count +=  1
        cgate.all.append( self )
    def is_external(self):
        return len( self.groups ) < 5
        
middle = circut.split(":")[1]
for gate in middle.split(","):
    m = re.match(r"([\d]+)([RL])([\d]+)([RL])0#([\d])+([RL])([\d]+)([RL])", gate )
    if m:
        cgate( gate, m.groups() )
        print "# %20s"%gate, m.groups()
    else:
        m = re.match("X([\d])+([RL])0#X([\d])+([RL])", gate )
        if m:
            cgate( gate, m.groups() )
            print "# %20s"%gate, m.groups()
        else:
            print "# %20s"%gate, "no match"

for g in  cgate.all :
    if g.is_external():
        print "# External Gate", g.text, g.groups
        print 'g%d -> g%s [label="I1 %s"];'%(g.id, g.groups[0], g.groups[1] )
        print 'g%d -> g%s [label="o1 %s"];'%(g.id, g.groups[2], g.groups[3] )
    else:
        print "#", g.text, g.groups
        print 'g%d -> g%s [label="I1 %s"];'%(g.id, g.groups[0], g.groups[1] )
        print 'g%d -> g%s [label="I2 %s"];'%(g.id, g.groups[2], g.groups[3] )
        print 'g%d -> g%s [label="o1 %s"];'%(g.id, g.groups[4], g.groups[5] )
        print 'g%d -> g%s [label="o2 %s"];'%(g.id, g.groups[6], g.groups[7] )




print "}"
