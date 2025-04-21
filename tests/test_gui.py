import unittest
from PyQt5.QtWidgets import QApplication
from src.gui import MainWindow
from src.gui.widgets import (
    CircuitView, 
    HistogramView, 
    BlochView,
    StateCityView, 
    ControlPanel
)
from src.core.quantum_experiment import QuantumExperiment

class TestGUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])
        cls.window = MainWindow()

    @classmethod
    def tearDownClass(cls):
        cls.window.close()
        cls.app.quit()

    def test_main_window_creation(self):
        """Test if main window is created properly"""
        self.assertIsInstance(self.window, MainWindow)
        self.assertEqual(self.window.windowTitle(), "Quantum Circuit Simulator")

    def test_widget_initialization(self):
        """Test if all widgets are initialized properly"""
        self.assertIsInstance(self.window.circuit_view, CircuitView)
        self.assertIsInstance(self.window.histogram_view, HistogramView)
        self.assertIsInstance(self.window.bloch_view, BlochView)
        self.assertIsInstance(self.window.state_city_view, StateCityView)
        # self.assertIsInstance(self.window.Quantum_state, QLabel)
        self.assertIsInstance(self.window.control_panel, ControlPanel)

    def test_control_panel_settings(self):
        """Test control panel initial settings"""
        self.assertEqual(self.window.control_panel.qubit_selector.minimum(), 1)
        self.assertEqual(self.window.control_panel.qubit_selector.maximum(), 10)  # Changed from 1 to 9 for 10 qubits

    def test_quantum_experiment_integration(self):
        """Test quantum experiment integration"""
        self.assertIsInstance(self.window.experiment, QuantumExperiment)
        self.assertEqual(self.window.experiment.num_qubits, 10)  # Changed from 2 to 10

    def test_control_panel_actions(self):
        """Test control panel button connections"""
        self.assertTrue(self.window.control_panel.hadamard_button.isEnabled())
        self.assertTrue(self.window.control_panel.cnot_button.isEnabled())
        self.assertTrue(self.window.control_panel.entangle_button.isEnabled())
        self.assertTrue(self.window.control_panel.reset_button.isEnabled())
        self.assertTrue(self.window.control_panel.measure_button.isEnabled())
        self.assertTrue(self.window.control_panel.simulate_button.isEnabled())

if __name__ == '__main__':
    unittest.main()