

from pypower.api import case9, ppoption, runpf
import numpy as np

temp = case9()


temp = case9()
ppopt = ppoption(OUT_ALL=0)

(r, s) = runpf(temp, ppopt)
#(r, s) = runpf(temp)

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

print type(r["success"])

print (1-10.0/100)
