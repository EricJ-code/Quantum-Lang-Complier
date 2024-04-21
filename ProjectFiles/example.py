import numpy as np

class qubit():
    def __init__(self, state_code):
        self.states = []
        for num in state_code:
            if num == 0:
                self.states.append([1, 0])
            elif num == 1:
                self.states.append([0, 1])
            elif num == 'i':
                self.states.append(['i'])
    
    def print_qubit(self):
        for state in self.states:
            print(state, end="")
        print("")

q = qubit([0 , 1, 1, 0, 'i'])
q.print_qubit()

class gate():
    def __init__(self):
        self.h_math = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]]);
    def h(self, qubit, super_pos=False):
        results = []
        if super_pos == False:
            for state in qubit.states:
                if state[0] == 'i':
                    results.append('i')
                else:
                    results.append(np.dot(state, self.h_math))
        elif super_pos == True:
            for state in qubit.states:
                if state[0] == 'i':
                    results.append('i')
                else:
                    results.append(np.dot(state, self.h_math)**2)

g = gate()
g.h(q)
g.h(q,True)