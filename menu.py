######################
### Stability code ###
######################

#Copy the code below to the menu.py file in the .nuke folder

###################
### LOGO CLASS ### 
##################

from PySide2 import QtCore, QtGui, QtWidgets, QtSvg, QtXml

class logo(QtWidgets.QWidget):
    def __init__(self, node):
        super(self.__class__, self).__init__()

        self.node = node
        self.setFixedSize(140, 60)  # Set fixed size for the widget

    def paintEvent(self, e):
        # Initialize Painter
        painter = QtGui.QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        svg = self.node.knob('svg_knob').value()
        # Render Map
        rect = QtCore.QRect(0, 0, self.width(), self.height())
        renderer = QtSvg.QSvgRenderer(QtCore.QXmlStreamReader(svg), self)
        renderer.setViewBox(rect)  # Set the viewBox to the widget's rectangle
        renderer.render(painter, rect)

    def preserveAspectRatio(self):
        return True

    def sizeHint(self):
        return QtCore.QSize(140, 60)  # Return fixed size

    def makeUI(self):
        return self

#########################
### Animation Prompts ### 
#########################

import json
from PySide2 import QtCore, QtGui, QtWidgets, QtSvg

class anim_prompts(QtWidgets.QWidget):

    def __init__(self, node):
        super(self.__class__, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
        self.setMinimumHeight(150)
        self.table = QtWidgets.QTableWidget(2, 3)
        self.table.setAlternatingRowColors(True)
        self.table.itemChanged.connect(self.store_value)

        self.node = node


        # Set some default values for the 'animation_prompts' knob
        if not self.node.knob('animation_prompts').value():
            default_values = {0: "A cyberpunk futuristic colourful crowded luxurious pedestrian street avenue hi-tech at morning time, blue neon lights, ray tracing, hdr, realistic shaded, extremely detailed, sharp focus, soft lighting, sunny"}
            self.node.knob('animation_prompts').setValue(json.dumps(default_values))


        self.table.setHorizontalHeaderLabels(['Frame', 'Prompt', ' '])
        self.table.setColumnWidth(0, 42)
        self.table.setColumnWidth(2, 64)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        # Add delete logo
        for row in range(self.table.rowCount()):
            self.addDeleteButton(row)

        # Add the table to the layout
        self.layout.addWidget(self.table)

        # Add a button to add rows
        self.addRowButton = QtWidgets.QPushButton("Add a Prompt", self)
        self.addRowButton.clicked.connect(self.addRow)
        #self.addRowButton.setContentsMargins(10, 10, 10, 10)  # Add margins
        self.layout.addWidget(self.addRowButton)

        # Update the table from the knobs
        self.updateTableFromKnobs()

    def makeUI(self):
        return self

    def store_value(self):
        # Create a dictionary from the table
        self.data = {}
        for row in range(self.table.rowCount()):
            item0 = self.table.item(row, 0)
            item1 = self.table.item(row, 1)
            if item0 is not None and item1 is not None:
                self.data[int(item0.text())] = item1.text()
            
        # Convert the dictionary to a string and store it in a Nuke knob
        self.node.knob('animation_prompts').setValue(json.dumps(self.data))


    def load_value(self):
        # Load the dictionary from the Nuke knob and convert it back to a dictionary
        self.data = json.loads(self.node.knob('animation_prompts').value())

    # Method to add a row
    def addRow(self):
        currentRowCount = self.table.rowCount()  
        self.table.insertRow(currentRowCount)
        
        # Calculate the maximum frame number currently in the table
        max_frame = max(int(self.table.item(row, 0).text()) for row in range(currentRowCount)) if currentRowCount > 0 else -1
        
        # Initialize the new row with frame number one more than the maximum
        self.initializeRow(currentRowCount, max_frame + 1)
        
        self.addDeleteButton(currentRowCount)  
        self.store_value()

    def initializeRow(self, row, frame):
        # Initialize items 
        self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(frame))) 
        self.table.setItem(row, 1, QtWidgets.QTableWidgetItem("a cute unicorn"))

    # Method to add a delete logo_class_button
    def addDeleteButton(self, row):
        deleteButton = QtWidgets.QPushButton("Delete", self)
        deleteButton.clicked.connect(lambda: self.table.removeRow(row))
        deleteButton.clicked.connect(lambda: self.removeRow(row))
        self.table.setCellWidget(row, 2, deleteButton)

    def removeRow(self, row):
        self.table.removeRow(row)  
        self.store_value() # Update storage

    def disconnectSignals(self):
        self.table.itemChanged.disconnect(self.store_value)

    def updateTableFromKnobs(self):
        # Disconnect the itemChanged signal to prevent it from being triggered while updating the table
        self.table.itemChanged.disconnect(self.store_value)

        # Clear the table
        self.table.setRowCount(0)

        # Load the dictionary from the 'animation_prompts' knob and convert it back to a dictionary
        self.data = json.loads(self.node.knob('animation_prompts').value())

        # Add rows to the table based on the dictionary
        for frame, prompt in self.data.items():
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(self.table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(str(frame)))
            self.table.setItem(self.table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(prompt))
            self.addDeleteButton(self.table.rowCount() - 1)

        # Reconnect the itemChanged signal
        self.table.itemChanged.connect(self.store_value)

#############################
### END OF STABILITY CODE ###
#############################