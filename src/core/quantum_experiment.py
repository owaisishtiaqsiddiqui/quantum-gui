from math import pi
from qiskit.circuit.library import QFT
from qiskit.providers.fake_provider import GenericBackendV2, generic_backend_v2
generic_backend_v2._NOISE_DEFAULTS["cx"] = (5.99988e-06, 6.99988e-06, 1e-5, 5e-3)

from qiskit import transpile, QuantumCircuit
from qiskit.circuit import Gate
from qiskit.converters import circuit_to_dag
from qiskit.transpiler import CouplingMap, StagedPassManager, PassManager, AnalysisPass, TransformationPass
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.transpiler.preset_passmanagers.common import generate_unroll_3q, generate_embed_passmanager
from qiskit.quantum_info import hellinger_fidelity
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.dagcircuit import DAGCircuit
#from qiskit_ibm_runtime.fake_provider import FakeTorino

# Transpiler Passes
## Layout passes
from qiskit.transpiler.passes.layout.csp_layout import CSPLayout
from qiskit.transpiler.passes.layout.dense_layout import DenseLayout
from qiskit.transpiler.passes.layout.sabre_layout import SabreLayout
from qiskit.transpiler.passes.layout.vf2_layout import VF2Layout
from qiskit.transpiler.passes.layout.trivial_layout import TrivialLayout

## Routing passes
from qiskit.transpiler.passes.routing.basic_swap import BasicSwap
from qiskit.transpiler.passes.routing.lookahead_swap import LookaheadSwap
from qiskit.transpiler.passes.routing.sabre_swap import SabreSwap
#from qiskit.transpiler.passes.routing.stochastic_swap import StochasticSwap
from qiskit.transpiler.passes.routing.star_prerouting import StarPreRouting

## Synthesis passes (passes for the translation stage)
from qiskit.circuit import SessionEquivalenceLibrary
from qiskit.circuit.equivalence_library import SessionEquivalenceLibrary
from qiskit.transpiler.passes.basis.basis_translator import BasisTranslator
from qiskit.transpiler.passes.synthesis.high_level_synthesis import HighLevelSynthesis
### The next pass could also be considered an optimization pass.
from qiskit.transpiler.passes.synthesis.unitary_synthesis import UnitarySynthesis

## Optimization passes
from qiskit.transpiler.passes.optimization.collect_1q_runs import Collect1qRuns
from qiskit.transpiler.passes.optimization.collect_2q_blocks import Collect2qBlocks
from qiskit.transpiler.passes.optimization.consolidate_blocks import ConsolidateBlocks
from qiskit.transpiler.passes.optimization.optimize_1q_gates import Optimize1qGates
from qiskit.transpiler.passes.optimization.commutative_cancellation import CommutativeCancellation
#from qiskit.transpiler.passes.optimization.cx_cancellation import CXCancellation

#from qiskit_aer.noise import NoiseModel, depolarizing_error, thermal_relaxation_error, ReadoutError
#from qiskit_aer import AerSimulator

#from qiskit_ibm_runtime import QiskitRuntimeService

import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Clifford, Statevector
from qiskit.visualization import plot_histogram, plot_bloch_multivector, plot_state_qsphere, plot_state_city ,plot_state_hinton, plot_circuit_layout, plot_gate_map

class QuantumExperiment:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.circuit = QuantumCircuit(num_qubits, num_qubits)
        self.backend = AerSimulator(method='statevector')

    def apply_hadamard(self, qubit_index):
        self.circuit.h(qubit_index)

    def apply_cnot(self, control_qubit, target_qubit):
        self.circuit.cx(control_qubit, target_qubit)

    def entangle(self, qubit1, qubit2):
        self.circuit.h(qubit1)
        self.circuit.cx(qubit1, qubit2)

    def reset_circuit(self):
        """Reset the quantum circuit to its initial state."""
        self.circuit = QuantumCircuit(self.num_qubits, self.num_qubits)

    def measure_all(self):
        self.circuit.measure(range(self.num_qubits), range(self.num_qubits))

    def simulate(self):
        backend = AerSimulator(method='statevector')
        transpiled_qc = transpile(self.circuit, backend)
        job = backend.run(transpiled_qc, shots=1000)
        result = job.result()
        return result.get_counts(transpiled_qc)

    def show_circuit(self):
        return self.circuit.draw(
            output='mpl',
            style={
                'figwidth': 2,
                'figheight': 2,
                'fontsize': 14
            }
        )
    
    # def get_statevector(self):
    #     """Simulate the circuit and return the statevector."""
    #     job = transpile(self.circuit, self.backend)
    #     result = job.result()
    #     return result.get_statevector()
    def get_statevector(self):
        """Simulate the circuit and return the statevector."""
        transpiled_circuit = transpile(self.circuit, self.backend)
        job = self.backend.run(transpiled_circuit)
        result = job.result()
        return result.get_statevector()
    
    # def plot_qsphere(self):
    #     """Return a QSphere plot of the current state."""
    #     statevector = self.get_statevector()
    #     return plot_state_qsphere(statevector)
    
    def plot_histogram(self, counts):
        # Plot measurement results histogram
        fig = plot_histogram(counts)
        return fig
    
    def plot_bloch(self):
        # Get statevector for Bloch sphere visualization
        backend = AerSimulator()  # Remove method specification
        transpiled_qc = transpile(self.circuit, backend)
        # Add save_statevector instruction
        transpiled_qc.save_statevector()
        job = backend.run(transpiled_qc)
        result = job.result()
        statevector = result.get_statevector()
        return plot_bloch_multivector(statevector)
    
    def plot_state_city(self):
        # Get statevector for city plot
        backend = AerSimulator()  # Remove method specification
        transpiled_qc = transpile(self.circuit, backend)
        # Add save_statevector instruction
        transpiled_qc.save_statevector()
        job = backend.run(transpiled_qc)
        result = job.result()
        statevector = result.get_statevector()
        return plot_state_city(statevector)
    
    # def plot_Quantum_state(self):
    #     """Return a Hinton plot of the current state."""
    #     statevector = self.get_statevector()
    #     return plot_state_hinton(statevector)