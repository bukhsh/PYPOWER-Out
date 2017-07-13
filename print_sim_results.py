import os

from pypower.api import printpf  # PYPOWER stuff

"""
s = success (=0 diverged, =1 converged)
n_out= outage number
r= results structure
flag_v = voltage violation flag (=0 voltages are within tol)
flag_p = real power violation flag (=0 real pow gen are within tol)
flag_q = reactive power violation flag (=0 reactive pow gen are within tol)
flag_l = line limit violation flag (=0 line limits are within tol)
"""
def print_sim_results(s, n_out,r, flag_v, flag_p, flag_q, flag_l):
    ##########################
    #open file to write output
    #########################
    path = "/home/hwb14223/Python/sim_outages/results" #path to write output
    filename = "outage" + str(n_out)
    fullpath = os.path.join(path, filename)
    f = open(fullpath, 'w')
    if s == 1:
        if flag_v == 0 and flag_p == 0 and flag_q == 0 and flag_l == 0:
            f.write('Load Flow ***converged*** and all values are within limits\n')
        else:
            f.write('Load flow ***converged*** but it lead to following violations:\n')
            f.write('%d buses have voltage issues:\n' % flag_v)
            f.write('%d generator buses have out of value real power generation:\n' % flag_p)
            f.write('%d generator buses have out of value reactive power generation:\n' % flag_q)
            f.write('%d lines have apprent power lim violation:' % flag_l)
    else:
        f.write('***Load flow diverged***')
    #######output######
    printpf(r,f)
    f.close()


