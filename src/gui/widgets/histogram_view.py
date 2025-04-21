from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

class HistogramView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.canvas = None
        self.setLayout(self.layout)

    def update_histogram(self, histogram_figure):
        if self.canvas:
            self.layout.removeWidget(self.canvas)
            self.canvas.deleteLater()
        
        self.canvas = FigureCanvasQTAgg(histogram_figure)
        self.layout.addWidget(self.canvas)