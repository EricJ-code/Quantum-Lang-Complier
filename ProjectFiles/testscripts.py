import unittest
import numpy as np
from depency_classes.py import qubit, gate

class TestQuantumComputing(unittest.TestCase):
    def test_qubit_initialization(self):
        q = qubit([0, 1])
        expected_state_0 = np.array([[1], [0]])
        expected_state_1 = np.array([[0], [1]])
        np.testing.assert_array_equal(q.states[0], expected_state_0)
        np.testing.assert_array_equal(q.states[1], expected_state_1)

    def test_qubit_str(self):
        q = qubit([0, 1])
        output = str(q)
        expected_output = ("-----------------\n"
                           "| [Real + Imag] |\n"
                           "|T[1.00 + 0.00i]|\n"
                           "|B[0.00 + 0.00i]|\n"
                           "-----------------\n"
                           "|T[0.00 + 0.00i]|\n"
                           "|B[1.00 + 0.00i]|\n"
                           "-----------------\n")
        self.assertEqual(output, expected_output)

    def test_gate_hadamard_on_single_qubit(self):
        q = qubit([0])
        g = gate()
        g.default_gates('h', q)
        expected_result = (1 / np.sqrt(2)) * np.array([[1], [1]])
        np.testing.assert_array_almost_equal(g.results[0], expected_result)

    def test_gate_CNOT(self):
        # Testing CNOT gate assuming correct Kron product and gate implementation.
        # CNOT should not change the state of first qubit (control qubit |0>) and thus not the second qubit (target)
        q = qubit([0, 0])  # Initial state |00>
        g = gate()
        g.default_gates('CNOT', q)
        expected_result = np.array([[1], [0], [0], [0]])  # still |00>
        np.testing.assert_array_equal(g.results[0], expected_result)

    def test_superposition_flag(self):
        # Test that the superposition flag does not alter the expected results in an unexpected way
        q = qubit([0])
        g = gate()
        g.super_pos = True
        g.default_gates('h', q)
        expected_result = (1 / np.sqrt(2)) ** 2 * np.array([[1], [1]])  # Element-wise square
        np.testing.assert_array_almost_equal(g.results[0], expected_result)

    def test_keep_results(self):
        q = qubit([1])
        g = gate()
        g.keep_results = True
        g.default_gates('x', q)
        expected_state = np.array([[1], [0]])  # |1> after X becomes |0>
        np.testing.assert_array_equal(q.states[0], expected_state)

if __name__ == '__main__':
    unittest.main()
