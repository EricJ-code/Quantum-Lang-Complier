#This is to use as an example for demo purposes
import depency_classes as sdc

# Qubit(s) Class
q = sdc.qubit([1])
print(q)

u = sdc.qubit([1, 0])
print(u)

#Gate Class
g = sdc.gate()
g.default_gates('h', q)
print(g)
g.default_gates('x', q)
print(g)
g.default_gates('y', q)
print(g)
g.default_gates('z', q)
print(g)

#Strech Goals
# Saving a state indiv
q.states = g.results

#Saving toggle
g.keep_results = True
g.keep_results = False

#Super Pos toggle
g.super_pos = True
g.super_pos = False



# ; This is to use as an example for demo purposes

# ; Qubit(s) class

# |0> q   ;(1, 0)
# observe q

# |1>u   ;(0, 1)
# observe u

# |00>b  ;(1, 0), (1, 0)
# observe b



# ; Gate class

# #g

# g.h q
# observe q
# g.x q
# observe q
# g.y q 
# observe q
# g.z q
# observe q

# g.h u
# observe u
# g.x u 
# observe u
# g.y u 
# observe u
# g.z u 
# observe u

# g.CNOT b 

# g.CNOT i 


# ; Strech Goals

# ;Saving a state indiv

# q save g

# ;Saving toggle
# g saving
# g !saving

# ;Super Pos toggle
# g super
# g !super