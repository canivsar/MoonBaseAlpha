import  random


Besttruth = {
  (0, 0) : [0, 2]
, (0, 1) : [2, 2]
, (0, 2) : [2, 1]
, (1, 0) : [1, 1]
, (1, 1) : [2, 0]
, (1, 2) : [0, 0]
, (2, 0) : [2, 2]
, (2, 1) : [0, 2]
, (2, 2) : [1, 2]
}


truth = {
  (0, 0) : [2, 1]
, (0, 1) : [1, 1]
, (0, 2) : [0, 2]
, (1, 0) : [2, 2]
, (1, 1) : [2, 2]
, (1, 2) : [1, 1]
, (2, 0) : [2, 0]
, (2, 1) : [0, 1]
, (2, 2) : [0, 0]
}




input1 =  [0,2,1,2,0,1,1,2,1,0,0,0,0,2,1,2,0]

input2 =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

output1 = [0,1,0,2,2,2,1,0,0,0,2,2,1,1,0,2,2]

maxi=0;


def LogicGateA (inputTupple):
    return truth[inputTupple]



def PrintTruth (tt):
    mylist=[]
    kk = tt.keys()
    kk.sort()
    for t in kk:
        mylist.append( tt[t])
    print mylist


def TryThis ():
    global truth
    global input2
    global maxi
    truth = Besttruth
#    print truth

#    truth[(random.randint(0,2),random.randint(0,2))]=[random.randint(0,2),random.randint(0,2)]
    truth[(0,0)]=[random.randint(0,2),random.randint(0,2)]
    truth[(0,1)]=[random.randint(0,2),random.randint(0,2)]
    truth[(0,2)]=[random.randint(0,2),random.randint(0,2)]



    for i in range(len(input1)):
        global input2
        out1,out2 = LogicGateA((input1[i],input2[i]))
        if out1 != output1[i]:
            return 0
        input2[i+1] = out2
        if i > maxi:
            maxi=i
            print maxi
            print input1
            print input2
            PrintTruth( truth)
            print truth
    return 1



def main ():
    for xx in range(1000000):
        if (TryThis()):
            #PrintTruth( truth)
            print input2
    print "done"


main()



