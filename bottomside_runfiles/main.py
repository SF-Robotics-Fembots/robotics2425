import lgpio
import pygame
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit
import time
import threading
import socket


#import threaded files
import thrusters

# library setup
pygame.init()
i2c = busio.I2C(board.SCL, board.SDA)
shield = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)
shield.frequency = 100

#global ip variable setup
global ip_server
ip_server = "192.168.1.100"
    

thrusterCode = threading.Thread(target=thrusters2324.main, args = (ip_server,))

thrusterCode.start()

thrusterCode.join()
