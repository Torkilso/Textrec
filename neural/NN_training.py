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

def trainNetwork(files_path, out):
    img_files = os.listdir(files_path)
    for file_ in img_files:
        label_int = ord(file_[0])
        label_bin = "{0:b}".format(label_int)
        for x in range(0,out-len(label_bin)):
            label_bin = "0" + label_bin
            pass

        targets = numpy.zeros(out) + 0.01
        for x in range(0, out):
            if(label_bin[x] == "1"):
                targets[x] = 0.99
            pass

        img_array = scipy.misc.imread(files_path + "/" + file_, flatten=True)
        img_data = 255.0 - img_array.reshape(784)
        img_data = (img_data / 255.0*0.99)+0.01

        n.train(img_data, targets)
        pass
    pass

def writeWeights(who_path, wih_path, network):

    who_file_w = open(who_path, "w")
    for row in network.who:
        for value in row:
            who_file_w.write(str(value) + ",")
            pass
        who_file_w.write("\n")
        pass
    who_file_w.close()

    wih_file_w = open(wih_path, "w")
    for row in network.wih:
        for value in row:
            wih_file_w.write(str(value) + ",")
            pass
        wih_file_w.write("\n")
        pass
    wih_file_w.close()
    pass

# Specify amount of inputnodes, hidden nodes and outputnodes
inputs = 784
hidden = 300
outputs = 8

# Learningrate
lr = 0.3

n = neuralNetwork(inputs, hidden, outputs, lr)

# Set the weights
setWeights("./weights_who.txt", "./weights_wih.txt", n, outputs, hidden, inputs)

# Train the network
trainNetwork("./handwritten/letters/small", outputs)
trainNetwork("./handwritten/letters/capital", outputs)
trainNetwork("./handwritten/numbers", outputs)

# Save the weights
writeWeights("./weights_who.txt", "./weights_wih.txt", n)
