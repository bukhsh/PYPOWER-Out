
import tol_pf_sol
from pypower.api import case9
import numpy as np
import print_sim_results

def check_sol(n_out,r):
    (v_tol, pG_tol, qG_tol, br_tol) = tol_pf_sol.tol_pf_sol()
    voltage = r["bus"][:, 7]
    angle = r["bus"][:, 8]
    real_gen = r["gen"][:, 1]
    reactive_gen = r["gen"][:, 2]
    real_flow_fr = r["branch"][:, 13]
    real_flow_to = r["branch"][:, 15]
    reactive_flow_fr = r["branch"][:, 14]
    reactive_flow_to = r["branch"][:, 16]
    apparent_power_flow_fr = np.sqrt(real_flow_fr**2 + reactive_flow_fr**2)
    apparent_power_flow_to = np.sqrt(real_flow_to**2 + reactive_flow_to**2)
    temp = case9()
    nbus = len(temp["bus"])
    ngen = len(temp["gen"])
    nbr = len(temp["branch"])
    #flags for deviation
    flag_v = 0
    flag_p = 0
    flag_q = 0
    flag_l = 0
    #check voltage
    for i in range(0,nbus):
        if r["bus"][i, 7] < (1-v_tol/100) or r["bus"][i, 7] > (1+v_tol/100):
            flag_v += 1
    #check gen bounds
    for i in range(0,ngen):
        if r["gen"][i, 1] < (1-pG_tol/100)*temp["gen"][i,9] or r["gen"][i, 1] > (1+pG_tol/100)*temp["gen"][i,8]:
            flag_p += 1
        if r["gen"][i, 2] < (1-qG_tol/100)*temp["gen"][i,4] or r["gen"][i, 2] > (1+qG_tol/100)*temp["gen"][i,3]:
            flag_q += 1
    #check branch flows
    for i in range(0,nbr):
        if apparent_power_flow_fr[i]>(1+br_tol/100)*temp["branch"][i,5] or (1+br_tol/100)*apparent_power_flow_to[i]>temp["branch"][i,5]:
            flag_l += 1
    print_sim_results.print_sim_results(r["success"], n_out,r, flag_v, flag_p, flag_q, flag_l)


