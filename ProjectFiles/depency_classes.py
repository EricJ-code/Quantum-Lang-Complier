import numpy as np

class qubit():
    def __init__(self, state_code):
        self.states = []
        for num in state_code:
            if num == 0:
                self.states.append(np.array([[1], [0]]))
            elif num == 1:
                self.states.append(np.array([[0], [1]]))
    def __str__(self) -> str:
        s = "-----------------\n"
        s += "| [Real + Imag] |\n"
        for state in self.states:
            real_part_0 = float(state[0].real)
            imag_part_0 = float(state[0].imag)
            real_part_1 = float(state[1].real)
            imag_part_1 = float(state[1].imag)

            s += "|T[{:1.2f} + {:1.2f}i]|\n".format(real_part_0, imag_part_0)
            s += "|B[{:1.2f} + {:1.2f}i]|\n".format(real_part_1, imag_part_1)
            s += "-----------------\n"
        return s



class gate():
    def __init__(self):
        self.keep_results = False;
        self.super_pos = False;

        self.results = np.array([])
        self.h_math = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]);
        self.x_math = np.array([[0, 1], [1, 0]])
        self.y_math = np.array([[0, -1j], [1j, 0]])
        self.z_math = np.array([[1, 0], [0, -1]])
        self.CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

    def __str__(self) -> str:
        s = "-----------------\n"
        s += "| [Real + Imag] |\n"
        for result in self.results:
            for row in result:
                real_part = float(row[0].real)
                imag_part = float(row[0].imag)
                s += "| [{:1.2f} +{:1.2f}i] |\n".format(real_part, imag_part)
            s += "-----------------\n"
        return s
    
    def default_gates(self, gate, qubit):
        dot_math = 0
        self.results = []
        match gate:
            case 'h':
                dot_math = self.h_math
            case 'x':
                dot_math = self.x_math
            case 'y':
                dot_math = self.y_math
            case 'z':
                dot_math = self.z_math
            case 'CNOT':
                if len(qubit.states) % 2 == 0:
                    self.results = []
                    for i in range(0, len(qubit.states), 2):
                        joint_state = np.kron(qubit.states[0], qubit.states[1])
                        self.results.append(np.dot(self.CNOT, joint_state))
                    if self.keep_results:
                        qubit.states = self.results
                    return

        for state in qubit.states:
            result = np.dot(dot_math, state)
            self.results.append(result if not self.super_pos else result**2)

        if self.keep_results:
            qubit.states = self.results
        
    
