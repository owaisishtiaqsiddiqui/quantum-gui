from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QPushButton, QLabel

class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Qubit selection
        self.qubit_label = QLabel("Select Qubit:")
        self.qubit_selector = QSpinBox()
        self.qubit_selector.setMinimum(0)

        # Control buttons
        self.hadamard_button = QPushButton("Apply Hadamard")
        self.cnot_button = QPushButton("Apply CNOT")
        self.entangle_button = QPushButton("Apply Entangle")
        self.test_reset_button = QPushButton("Test Reset")
        self.measure_button = QPushButton("Measure")
        self.simulate_button = QPushButton("Simulate")
        self.Quantum_state = QPushButton("Show Quantum_state")
        #self.qsphere_button = QPushButton("Show QSphere")

        # Add widgets to layout
        self.layout.addWidget(self.qubit_label)
        self.layout.addWidget(self.qubit_selector)
        self.layout.addWidget(self.hadamard_button)
        self.layout.addWidget(self.cnot_button)
        self.layout.addWidget(self.entangle_button)
        self.layout.addWidget(self.test_reset_button)
        self.layout.addWidget(self.measure_button)
        self.layout.addWidget(self.simulate_button)
        #self.layout.addWidget(self.qsphere_button)
        self.layout.addWidget(self.Quantum_state)
        self.layout.addStretch()

    def set_max_qubit(self, num_qubits=2):
        self.qubit_selector.setMaximum(num_qubits)