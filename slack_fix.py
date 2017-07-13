

def slack_fix(temp):
    nbus = len(temp["bus"])  # number of buses
    for i in range(0, nbus + 1):
            if temp["bus"][i][1] == 2:
                temp["bus"][i][1] = 3
                return temp
