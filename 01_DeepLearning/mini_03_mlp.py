def hard_limit(net):
    return 1 if net > 0 else 0

def AND_gate(x1, x2):
    w1, w2, w3 = 1.0, 1.0, -1.5
    net = (x1 * w1) + (x2 * w2) + w3
    return hard_limit(net)

def OR_gate(x1, x2):
    w1, w2, w3 = 1.0, 1.0, -0.5
    net = (x1 * w1) + (x2 * w2) + w3
    return hard_limit(net)

def XOR_gate(x1, x2):
    y1 = AND_gate(x1, x2)
    y2 =OR_gate(x1, x2)
    w31, w32, w33 = -1.0, 1.0, -0.5
    net = (y1 * w31) + (y2 * w32) + w33
    return hard_limit(net)


print("XOR(0,0)=",XOR_gate(0,0))
print("XOR(0,1)=",XOR_gate(0,1))
print("XOR(1,0)=",XOR_gate(1,0))
print("XOR(1,1)=",XOR_gate(1,1))