import numpy as np

class qubit():
    def __init__(self, state_code):
        self.states = []
        for num in state_code:
            if num == 0:
                self.states.append([1, 0])
            elif num == 1:
                self.states.append([0, 1])
    def __str__(self) -> str:
        s= ""
        for state in self.states:
            s += ("[%1.4f %1.4f]" %(state[0], state[1]))
        return s



class gate():
    def __init__(self):
        self.results = np.array([])
        self.h_math = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]);
        self.x_math = np.array([[0, 1], [1, 0]])
        self.y_math = np.array([[0, -1j], [1j, 0]])
        self.z_math = np.array([[1, 0], [0, -1]])

    def __str__(self) -> str:
        s = ""
        for result in self.results:
            formatted_result = "[" + " ".join("{:1.4f}".format(elem) for elem in result.flatten()) + "] "
            s += formatted_result
        return s.strip()
    
    def default_gates(self, gate, qubit, super_pos=False, keep_results = False):
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

        if super_pos == False:
            for state in qubit.states:
                self.results.append(np.dot(state, dot_math))
        elif super_pos == True:
            for state in qubit.states:
                self.results.append(np.dot(state, dot_math)**2)
        if keep_results == True:
            qubit.states = self.results
        
    
