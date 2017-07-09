from NN import neuralNetwork
import scipy.misc
import os
import numpy

def setWeights(who_path, wih_path, network, out, hid, inp):
    who_file_r = open(who_path, "r")
    read_who = who_file_r.read()
    who_rows_read = read_who.split("\n")
    who_rows = who_rows_read[0:out]

    who_full = numpy.zeros((out,hid))

    for i in range (0,out):
        who_values = who_rows[i].split(",")
        for x in range (0,hid):
            who_full[i,x] = who_values[x]
            pass
        pass

    who_file_r.close()


    wih_file_r = open(wih_path, "r")
    read_wih = wih_file_r.read()

    wih_rows_read = read_wih.split("\n")
    wih_rows = wih_rows_read[0:hid]

    wih_full = numpy.zeros((hid,inp))

    for i in range (0,hid):
        wih_values = wih_rows[i].split(",")
        for x in range (0,inp):
            wih_full[i,x] = wih_values[x]
            pass
        pass

    wih_file_r.close()

    network.who = who_full
    network.wih = wih_full

    pass

def setUpAndGetNetwork():
    # Specify amount of inputnodes, hidden nodes and outputnodes
    inputs = 784
    hidden = 300
    outputs = 8
    # Learningrate
    lr = 0.3

    n = neuralNetwork(inputs, hidden, outputs, lr)
    #setWeights("./weights_who.txt", "./weights_wih.txt", n, outputs, hidden, inputs)
    
    return n