
import scipy.misc
import numpy

def queryNetwork(neuralNetwork):

    img_array = scipy.misc.imread("/home/torkilso/Documents/textrec/input.png", flatten=True)
    img_data = 255.0 - img_array.reshape(784)
    img_data = (img_data / 255.0*0.99)+0.01

    outputs = neuralNetwork.query(img_data)

    outputBinary = '0b'

    for output in outputs:
        print(output[0])
        if output[0] > 0.5:
            outputBinary = outputBinary + '1'
        else:
            outputBinary = outputBinary + '0'

    outputChar = int(outputBinary, 2)
    
    outputFinal = outputChar.to_bytes((outputChar.bit_length() + 7) // 8, 'big').decode()

    return outputFinal



