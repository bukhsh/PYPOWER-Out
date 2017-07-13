
import imout  # outage data
import numpy

outage = imout.imout()


def gen_out(temp, c):
    gen_bus = outage["gen"][c, 0]
    ind = numpy.where(temp["gen"][:, 0] == gen_bus)
    count = len(ind[0])
    for i in range(0, count):
        if temp["gen"][ind[0][i], 7] == 1:
            temp["gen"][ind[0][i], 7] = 0
            return temp
    return temp

