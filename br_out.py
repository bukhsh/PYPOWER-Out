
import imout  # outage data
import numpy

outage = imout.imout()


def br_out(temp, c):
    branch_out = outage["branch"][c, :]
    nbr_out = len(outage["branch"])
    for i in range(0, nbr_out):
        if (numpy.all(temp["branch"][i, 0:2] == branch_out)) == True:
            temp["branch"][i, 10] = 0
            return temp




