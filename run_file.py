#_author_="Bukhsh"

"""
run file for simulating outages
"""

from pypower.api import   ppoption, runpf  # PYPOWER stuff
#import   ppoption, runpf  # PYPOWER stuff
import imout  # outage data
import bus_out
import gen_out
import br_out
import check_sol
import print_sim_results
import os
import sys

#########Test cases#########
testdata = ["case9" , \
            "case9Q", \
            "case14", \
            "case24_ieee_rts", \
            "case30", \
            "case30pwl", \
            "case30Q",\
             "case39",\
             "case57",\
             "case118"]

cc = 0 #select test case

casea = __import__(testdata[cc])
###########################



ppopt = ppoption(OUT_ALL=0) #0=do not print output on screen
outage = imout.imout() #outage data

nbus_out = len(outage["bus"])
ngen_out = len(outage["gen"])
nbr_out = len(outage["branch"])

n_tot = nbus_out + ngen_out + nbr_out #total number of outages
success = [] #intialize success of load flow


n_out = 1 #initialize outage counter

# simulate bus outages
c = 0  # start counter
while c < nbus_out:
    temp = casea.casef() # initialize orignal testcase data
    temp = bus_out.bus_out(temp, c) #modify data according to outage
    (r, s) = runpf(temp, ppopt) #run load flow
    if s == 1:
        check_sol.check_sol(n_out, r) #check violations for convg case
    else:
        #print results if divergent case
        print_sim_results.print_sim_results(s, n_out, r, 0, 0, 0, 0)
    success.append(s)
    del s, r, temp
    c += 1
    n_out += 1

# Simulate gen outages
c = 0  # start counter
while c < ngen_out:
    temp = casea.casef()
    temp = gen_out.gen_out(temp, c)
    (r, s) = runpf(temp, ppopt)
    if s == 1:
        check_sol.check_sol(n_out, r)
    else:
        print_sim_results.print_sim_results(s, n_out, r, 0, 0, 0, 0)
    success.append(s)
    del s, r, temp
    c += 1
    n_out += 1


# Simulate line outages
c = 0  # start counter
#nbr_out = 2
while c < nbr_out:
    temp = casea.casef()
    temp = br_out.br_out(temp, c)
    (r, s) = runpf(temp, ppopt)
    if s == 1:
        check_sol.check_sol(n_out, r)
    else:
        print_sim_results.print_sim_results(s, n_out, r, 0, 0, 0, 0)
    success.append(s)
    #del s, r, temp
    c += 1
    n_out += 1


