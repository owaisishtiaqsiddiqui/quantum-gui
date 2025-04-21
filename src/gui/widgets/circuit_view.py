from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class CircuitView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.canvas = None
        self.setLayout(self.layout)

    def update_circuit(self, circuit_figure):
        if self.canvas:
            self.layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
        
        self.canvas = FigureCanvasQTAgg(circuit_figure)
        self.layout.addWidget(self.canvas)