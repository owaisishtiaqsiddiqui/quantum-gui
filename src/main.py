import sys
import os
from PyQt5.QtWidgets import QApplication

# Add the parent directory of the current file to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.gui import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

# import sys
# import os
# from PyQt5.QtWidgets import QApplication

# # Add the parent directory of the current file to sys.path
# #current_dir = os.path.dirname(os.path.abspath(__file__))
# #parent_dir = os.path.dirname(current_dir)
# #sys.path.append(parent_dir)

# from src.gui import MainWindow
# #from src.utils import configure_matplotlib_style
# # import sys
# # #from PyQt6.QtWidgets import QApplication
# # from PyQt5.QtWidgets import QApplication
# # import os
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# sys.path.append(os.getcwd())
# sys.path.append(os.path.join(os.getcwd(), 'src'))


# # from src.gui import MainWindow
# # from src.gui import configure_matplotlib_style


# def main():
#     #configure_matplotlib_style()
    
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()       
#     sys.exit(app.exec())

# if __name__ == '__main__':
#     main()
# # import sys
# # import os
# # from PyQt5.QtWidgets import QApplication
# # from src.gui import MainWindow

# # def resource_path(relative_path):
# #     """Get absolute path to resource, works for PyInstaller and normal runs."""
# #     if getattr(sys, 'frozen', False):
# #         base_path = sys._MEIPASS
# #     else:
# #         base_path = os.path.abspath(".")

# #     return os.path.join(base_path, relative_path)

# # def main():
# #     app = QApplication(sys.argv)
# #     window = MainWindow()
# #     window.show()
# #     sys.exit(app.exec())

# # if __name__ == '__main__':
# #     # Explicitly handle paths
# #     sys.path.append(resource_path('src'))

# #     main()
