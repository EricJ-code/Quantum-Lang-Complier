import depency_classes as sdc

qubit_name = sdc.qubit([1])
print(qubit_name)

qubit_name = sdc.qubit([1, 0])
print(qubit_name)

gate_name = sdc.gate()
gate_name.h(qubit_name)
gate_name.y(qubit_name)
print(gate_name)
