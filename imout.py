#outage data for case9
#_author_="Bukhsh"

"""
outage data PYPOWER test case
"""

from numpy import array


def imout():
    """
    abc
    """
    outage = {}
    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    outage["bus"] = array([
        [1],
        [2],
        [3]
    ])

    ## generator data
    # gen_bus
    outage["gen"] = array([
        [2],
        [3]
    ])

    ## branch data
    # fbus, tbus
    outage["branch"] = array([
        [1, 4],
        [4, 5],
        [5, 6],
        [3, 6],
        [6, 7],
        [7, 8],
        [8, 2],
        [8, 9],
        [9, 4]
    ])

    return outage
