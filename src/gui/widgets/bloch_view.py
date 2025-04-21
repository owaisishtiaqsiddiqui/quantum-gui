from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class BlochView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.canvas = None

    def update_bloch(self, figure):
        if self.canvas:
            self.layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
        
        self.canvas = FigureCanvasQTAgg(figure)
        self.layout.addWidget(self.canvas)