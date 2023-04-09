from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QLineEdit, QGridLayout, QPushButton ,QComboBox
from datetime import datetime
import sys

class SpeedCalculator(QWidget):
    # User interface object
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()
        self.units_combox = QComboBox()
        self.units_combox.addItems(['Imperial(mph)','English(km/h)'])
        time_label = QLabel("Time in mins:")
        self.time_line_edit = QLineEdit()
        calculate_button = QPushButton("Calculate Speed")
        # Call Calculate speed function on click event of button
        calculate_button.clicked.connect(self.calculatespeed)
        # Display Calcualted Speed
        self.output_label = QLabel("")

        # user interface layout
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.units_combox, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0 , 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        
        # initialize layout
        self.setLayout(grid)
    
 # Calculate Speed  funcation
    def calculatespeed(self):   
        speed = float(self.distance_line_edit.text())/float(self.time_line_edit.text())

        if self.units_combox.currentText() == 'Imperial(mph)':
             units = "mph"
             speed = round(speed*0.621371,2)
             
        if self.units_combox.currentText() == 'English(km/h)':
             units = "km/h"
             speed = round(speed,2)
             
        
        self.output_label.setText(f"{speed} {units} ")


     

app = QApplication(sys.argv)
age_Calculator = SpeedCalculator()
age_Calculator.show()
sys.exit(app.exec())


