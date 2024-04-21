import depency_classes as sdc

q = sdc.qubit([1])
print(q)

u = sdc.qubit([1, 0])
print(u)


g = sdc.gate()
g.default_gates('h', q)
print(g)
g.default_gates('x', q)
print(g)
g.default_gates('y', q)
print(g)
g.default_gates('z', q)
print(g)

