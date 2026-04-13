import numpy as np

def hard_limit(net):
    if net > 0:
        return 1
    else:
        return 0
    

def AND_gate(x1, x2):
    w1, w2, w3 = 1.0, 1.0, -1.5
    net = (x1 * w1) + (x2 * w2) + w3
    return hard_limit(net)

def OR_gate(x1, x2):
    w1, w2, w3 = 1.0, 1.0, -0.5
    net = (x1 * w1) + (x2 * w2) + w3
    return hard_limit(net)

def NOT_gate(x1):
    w1, w2 = -1.0, 0.5
    net = (x1 * w1) + w2
    return hard_limit(net)

print(f"AND(1,1)={AND_gate(1,1)}")
print(f"OR(0,1)={OR_gate(0,1)}")
print(f"NOT(1)={NOT_gate(1)}")