import math
import numpy
import scipy.special as special

# i - inputs
# h - hidden
# o - outputs
# t - target
# f - final
# e - errors

class neuralNetwork:
    def __init__(self, i, h, o, lr):
        self.ino = i
        self.hno = h
        self.ono = o

        self.lrn = lr

        self.wih = (numpy.random.normal(0.0, pow(self.hno, -0.5), (self.hno, self.ino)))
        self.who = (numpy.random.normal(0.0, pow(self.ono, -0.5), (self.ono, self.hno)))

        self.af = lambda x: special.expit(x)

        pass

    def train(self, i_list, t_list):
        i = numpy.array(i_list, ndmin=2).T
        t = numpy.array(t_list, ndmin=2).T

        h_i = numpy.dot(self.wih, i)
        h_o = self.af(h_i)

        f_i = numpy.dot(self.who, h_o)
        f_o = self.af(f_i)

        o_e = t - f_o
        h_e = numpy.dot(self.who.T, o_e)

        self.who += self.lrn * numpy.dot((o_e * f_o * (1.0 - f_o)),
                                        numpy.transpose(h_o))
        self.wih += self.lrn * numpy.dot((h_e * h_o * (1.0 - h_o)),
                                        numpy.transpose(i))

        pass

    def query(self, i_list):
        i = numpy.array(i_list, ndmin=2).T

        h_i = numpy.dot(self.wih, i)
        h_o = self.af(h_i)

        f_i = numpy.dot(self.who, h_o)
        f_o = self.af(f_i)

        return f_o
