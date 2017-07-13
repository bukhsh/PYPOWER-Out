
import imout  # outage data
import slack_fix  # fixes the issue with slack bus

outage = imout.imout()


def bus_out(temp, c):
    """-1 in the following command is because the indexing in python
    starts from 0 where as in Matpower bus numbers start from 1
    We need to fix this if the case bus numbers are not (1-n)
    consecutive integers"""
    bus_ind = int(outage["bus"][c][0] - 1)  # bus which needs to be isolated
    if temp["bus"][bus_ind][1] == 3:
        temp = slack_fix.slack_fix(temp)
    temp["bus"][bus_ind][1] = 4  # isolate the bus
    return temp
