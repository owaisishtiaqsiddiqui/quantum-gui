'''
Creates a main window with:

A circuit view and histogram on the left
Bloch sphere and state city visualizations on the right
Control panel with buttons and qubit selector
Connects the quantum backend with the GUI by:

Creating a QuantumExperiment instance
Updating visualizations when circuit changes
Handling user interactions through control panel
Provides methods to:

Apply Hadamard gates
Measure qubits
Simulate the circuit
Update all visualizations
Make sure you have all the required dependencies installed:

PyQt6
qiskit
matplotlib

The window layout is organized using QHBoxLayout
 and QVBoxLayout for a clean, professional appearance.
'''



from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSpinBox, QLabel
from PyQt5.QtCore import Qt
from .widgets import (
    CircuitView,
    HistogramView,
    BlochView,
    StateCityView,
    ControlPanel
)
from ..core import QuantumExperiment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quantum Circuit Simulator")
        self.resize(1200, 800)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Create left and right panels
        left_panel = QWidget()
        right_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        right_layout = QVBoxLayout(right_panel)

        # Initialize quantum experiment
        self.experiment = QuantumExperiment(num_qubits=2)

        # Create visualization widgets
        self.circuit_view = CircuitView()
        self.histogram_view = HistogramView()
        self.bloch_view = BlochView()
        self.state_city_view = StateCityView()
        # self.Quantum_state = Quantum_stateView()
        # self.Quantum_state.setText("Quantum State: " + str(self.experiment.get_statevector()))
        # self.Quantum_state.setAlignment(Qt.AlignCenter)
        # self.Quantum_state.setStyleSheet("font-size: 16px; font-weight: bold; color: blue;")
        

        # Create control panel
        self.control_panel = ControlPanel()
        self.control_panel.hadamard_button.clicked.connect(self.apply_hadamard)
        self.control_panel.cnot_button.clicked.connect(self.apply_cnot)
        self.control_panel.entangle_button.clicked.connect(self.entangle_qubits)
        self.control_panel.test_reset_button.clicked.connect(self.reset_circuit)
        self.control_panel.measure_button.clicked.connect(self.measure_circuit)
        self.control_panel.simulate_button.clicked.connect(self.simulate_circuit)
         # Add visualization buttons
        #self.control_panel.qsphere_button.clicked.connect(self.show_qsphere)
        #self.control_panel.Quantum_state.clicked.connect(self.Quantum_state)
        self.control_panel.set_max_qubit(num_qubits=2)

        # Add widgets to layouts
        left_layout.addWidget(self.circuit_view)
        left_layout.addWidget(self.histogram_view)
        right_layout.addWidget(self.bloch_view)
        right_layout.addWidget(self.state_city_view)
        #left_layout.addWidget(self.Quantum_stateView)
        
        # Add panels to main layout
        layout.addWidget(left_panel)
        layout.addWidget(right_panel)
        layout.addWidget(self.control_panel)

        # Initial circuit update
        self.update_circuit_view()

    def apply_hadamard(self):
        qubit = self.control_panel.qubit_selector.value()
        self.experiment.apply_hadamard(qubit)
        self.update_circuit_view()
        self.update_bloch_view()
        self.update_state_city_view()
    
    def apply_cnot(self):
        control_qubit = self.control_panel.qubit_selector.value()
        target_qubit = (control_qubit + 1) % self.experiment.num_qubits
        self.experiment.apply_cnot(control_qubit, target_qubit)
        self.update_circuit_view()
        self.update_bloch_view()
        self.update_state_city_view()
    
    def entangle_qubits(self):
        qubit1 = self.control_panel.qubit_selector.value()
        qubit2 = (qubit1 + 1) % self.experiment.num_qubits
        self.experiment.entangle(qubit1, qubit2)
        self.update_circuit_view()
        self.update_bloch_view()
        self.update_state_city_view()
    
    def reset_circuit(self):
        self.experiment.reset_circuit()
        self.update_circuit_view()
        self.update_bloch_view()
        self.update_state_city_view()

    def measure_circuit(self):
        self.experiment.measure_all()
        self.update_circuit_view()

    def simulate_circuit(self):
        counts = self.experiment.simulate()
        self.histogram_view.update_histogram(self.experiment.plot_histogram(counts))
    
    # def show_qsphere(self):
    #     """Display the QSphere visualization."""
    #     figure = self.experiment.plot_qsphere().figure
    #     self.display_figure(figure)

    def update_circuit_view(self):
        self.circuit_view.update_circuit(self.experiment.show_circuit())

    def update_bloch_view(self):
        self.bloch_view.update_bloch(self.experiment.plot_bloch())

    def update_state_city_view(self):
        self.state_city_view.update_state_city(self.experiment.plot_state_city())