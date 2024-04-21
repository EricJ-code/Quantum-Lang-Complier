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
            s += ("[%s %s]" %(state[0], state[1]))
        return s



class gate():
    def __init__(self):
        self.results = np.array([])
        self.h_math = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]);
        self.x_math = np.array([[0, 1], [1, 0]])
        self.y_math = np.array([[0, -1j], [1j, 0]])
        self.z_math = np.array([[0, 1], [1, 0]])

    def __str__(self) -> str:
        s= ""
        for state in self.results:
            s += ("[%1.4f %1.4f]" %(state[0], state[1]))
        return s
    
    def h(self, qubit, super_pos=False, keep_results = False):
        self.results = []
        if super_pos == False:
            for state in qubit.states:
                self.results.append(np.dot(state, self.h_math))
        elif super_pos == True:
            for state in qubit.states:
                self.results.append(np.dot(state, self.h_math)**2)
        if keep_results == True:
            qubit.states = self.results
    
    def x(self, qubit, super_pos=False, keep_results = False):
        self.results = []
        if super_pos == False:
            for state in qubit.states:
                self.results.append(np.dot(state, self.x_math))
        elif super_pos == True:
            for state in qubit.states:
                self.results.append(np.dot(state, self.x_math)**2)
        if keep_results == True:
            qubit.states = self.results

    def y(self, qubit, super_pos=False, keep_results = False):
        self.results = []
        if super_pos == False:
            for state in qubit.states:
                self.results.append(np.dot(state, self.y_math))
        elif super_pos == True:
            for state in qubit.states:
                self.results.append(np.dot(state, self.y_math)**2)
        if keep_results == True:
            qubit.states = self.results
        


