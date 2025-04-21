import unittest
from src.core import QuantumExperiment

class TestQuantumExperiment(unittest.TestCase):
    def setUp(self):
        """Set up test cases"""
        self.experiment = QuantumExperiment(num_qubits=2)

    def test_initialization(self):
        """Test if quantum experiment is initialized properly"""
        self.assertEqual(self.experiment.num_qubits, 2)
        self.assertIsNotNone(self.experiment.circuit)

    def test_hadamard_gate(self):
        """Test applying Hadamard gate"""
        initial_circuit_depth = self.experiment.circuit.depth()
        self.experiment.apply_hadamard(0)
        self.assertEqual(self.experiment.circuit.depth(), initial_circuit_depth + 1)
    
    def test_cnot_gate(self):
        """Test applying CNOT gate"""
        initial_circuit_depth = self.experiment.circuit.depth()
        self.experiment.apply_cnot(0, 1)
        self.assertEqual(self.experiment.circuit.depth(), initial_circuit_depth + 1)

    def test_entangle(self):
        """Test entangling two qubits"""
        initial_circuit_depth = self.experiment.circuit.depth()
        self.experiment.entangle(0, 1)
        self.assertEqual(self.experiment.circuit.depth(), initial_circuit_depth + 2)  # Two gates added: H and CNOT
        # Check if the circuit contains the correct gates
        gates = [inst.operation.name for inst in self.experiment.circuit.data]
        self.assertIn('h', gates)
        self.assertIn('cx', gates)

    def test_reset_circuit(self):
        """Test resetting the circuit"""
        self.experiment.apply_hadamard(0)
        self.experiment.apply_cnot(0, 1)
        # Check if the circuit has operations before reset
        self.assertGreater(len(self.experiment.circuit.data), 0)
        self.experiment.reset_circuit()
        # Check if the circuit is reset to initial state
        self.assertEqual(self.experiment.circuit.depth(), 0)
        # Check if the circuit is empty after reset
        self.assertEqual(len(self.experiment.circuit.data), 0)

    def test_measurement(self):
        """Test measurement operation"""
        self.experiment.measure_all()
        # Check if measurement operations were added for all qubits
        for qubit in range(self.experiment.num_qubits):
            self.assertTrue(any(inst.operation.name == 'measure' 
                              for inst in self.experiment.circuit.data
                              if qubit in inst.qubits))

    def test_simulation(self):
        """Test circuit simulation"""
        self.experiment.apply_hadamard(0)
        self.experiment.apply_cnot(0, 1)
        self.experiment.entangle(0, 1)
        self.experiment.reset_circuit()
        self.experiment.measure_all()
        counts = self.experiment.simulate()
        self.assertIsNotNone(counts)
        self.assertTrue(isinstance(counts, dict))

if __name__ == '__main__':
    unittest.main()