import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
import numpy as np
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from matplotlib import animation
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk 
from tkinter import ttk 
from tkinter import filedialog as fd
from tkinter import PhotoImage
import time

class TableWidgetDemo(QMainWindow):
   #self.table_widget=QTableWidget()
   global image
   def __init__(self):
      super().__init__()
      self.setWindowTitle("Fish Modeling")
      self.setGeometry(150, 150, 700, 400)

      self.table_widget = QTableWidget()
      self.table_widget.setRowCount(10)
      self.table_widget.setColumnCount(6)
      self.table_widget.setHorizontalHeaderLabels(["Year", "Region 1", "Region 2", "Region 3", "Region 4", "Region 5"])

      # Add a button to retrieve data
      self.button = QPushButton("Get Data")
      self.button2 = QPushButton("Animate")
      self.button.clicked.connect(self.convert_table_data_array)
      self.button2.clicked.connect(self.animate)

      layout = QVBoxLayout()
      layout.addWidget(self.table_widget)
      layout.addWidget(self.button)
      layout.addWidget(self.button2)

      container = QWidget()
      container.setLayout(layout)
      self.setCentralWidget(container)

   def convert_table_data_array(self):
         global np_array
         def get_column_values(self, column):
            column_val = []
            for row in range(self.table_widget.rowCount()):
               item = self.table_widget.item(row,column)
               if item is not None:
                  column_val.append(item.text())
            return column_val
         self.column_data1 = get_column_values(self, 1)
         self.column_data2 = get_column_values(self, 2)
         self.column_data3 = get_column_values(self, 3)
         self.column_data4 = get_column_values(self, 4)
         self.column_data5 = get_column_values(self, 5)
         np_array = np.array([self.column_data1, self.column_data2, self.column_data3, self.column_data4, self.column_data5])
         #print(np_array)
         return np_array
         #return self.column_data1
      
   def update_year(self):
      global text
      #region1 = np_array[0]
      self.label.configure(text=self.years[self.text])
      self.text = (self.text + 1) % len(self.years)
      self.parent.after(1000, self.update_year)

      self.convert_table_data_array()
      self.print_data()


   def print_data(self):
    #   if self.text == 1:
    #      if np_array[0][0] == 'y':
    #         print("in 2016, there is carp in region 1")
    #      else:
    #         print("NOOO")
    if self.text == 1:
        pixel_map = image.load() 
        width, height = image.size
        for i in range(width//2):  
            print

   def animate(self):
    # Step 1: Initialize the main window
    self.parent = tk.Tk()
    self.parent.title("Image in Frame Example")

    # Step 2: Create a frame within the main window
    frame = Frame(self.parent, width=700, height=850)
    frame.pack()

    # Step 3: Load the image using PIL
    image_path = "C:/Users/alyss/Downloads/waterRegioncarp.png" # Replace with your image path
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Step 4: Create a Canvas widget and add the image to it
    canvas = Canvas(frame, width=700, height=850)
    canvas.pack()

    # Add the image to the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Keep a reference to avoid garbage collection
    canvas.image = photo

      #changing year
    self.years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    self.text = 0
    self.label = tk.Label(self.parent, text=self.years[0])
    self.label.pack()
    self.update_year()
    #image
    #self.image_label.pack()
    self.parent.mainloop()
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWidgetDemo()
    window.show()
    sys.exit(app.exec_())