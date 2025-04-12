from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import pygetwindow as gw
import pyscreeze
import keyboard
import threading

width, height = 2000, 1800

#camera 1
url1 = 0
cam1 = cv2.VideoCapture('http://192.168.1.99:8080/stream')
cam1.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#camera 2
url2 = 1
cam2 = cv2.VideoCapture("http://192.168.1.99:8084/stream")
cam2.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam2.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#camera 3
url3 = 2
cam3 = cv2.VideoCapture("http://192.168.1.99:8082/stream")
cam3.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam3.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#create first window 
displayTop = Tk()
displayTop.title('top photosphere')
displayTop.bind('<Escape>', lambda e: displayTop.quit())

#create camera display on window 'displayTop'
cam1Display = Label(displayTop)
cam1Display.pack()

#creates second window
def new_window():
    print("opening new window")
    global cam2Display #can be accessed throughout program
    global cam3Display
    check = False #easier for opening both cameras without crashing

    #make second window
    displayBottom = tk.Toplevel()
    displayBottom.title('bottom photosphere')
    displayBottom.bind('<Escape>', lambda e: displayBottom.quit())

    #create camera display on 'displayBottom'
    cam2Display = Label(displayBottom)
    cam2Display.pack()
    print("made second display")

    displayMiddle = tk.Toplevel()
    displayMiddle.title('middle photosphere')
    displayMiddle.bind('<Escape>', lambda e: displayBottom.quit())

    #create camera display on 'displayBottom'
    cam3Display = Label(displayMiddle)
    cam3Display.pack()
    print("made third display")

    #changes check to open camera streams on windows
    check = True
    if check:
        open_camera() #runs first camera stream
        open_camera2() #runs second camera stream
        open_camera3()

#runs first cam stream
def open_camera():
    #read VideoCapture
    #print("getting frame 1")
    ret, frame1 = cam1.read()

    #updates image settings
    opencv_image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
    captured_image1 = Image.fromarray(opencv_image1)
    photo_image1 = ImageTk.PhotoImage(image = captured_image1)
    cam1Display.photo_image1 = photo_image1
    cam1Display.configure(image=photo_image1)

    #updates frame
    cam1Display.after(10, open_camera)

#runs second cam stream
def open_camera2():
    #read VideoCapture
    #print("getting frame 2")
    ret2, frame2 = cam2.read()

    #updates image settings
    opencv_image2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGBA)
    captured_image2 = Image.fromarray(opencv_image2)
    photo_image2 = ImageTk.PhotoImage(image = captured_image2)
    cam2Display.photo_image2 = photo_image2
    cam2Display.configure(image=photo_image2)

    #updates frames
    cam2Display.after(15, open_camera2)

def open_camera3():
    #read 
    #print("getting frame 2")
    ret3, frame3 = cam3.read()

    #updates image settings
    opencv_image3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGBA)
    captured_image3 = Image.fromarray(opencv_image3)
    photo_image3 = ImageTk.PhotoImage(image = captured_image3)
    cam3Display.photo_image3 = photo_image3
    cam3Display.configure(image=photo_image3)

    #updates frames
    cam3Display.after(15, open_camera3)

#screenshots frames when ready
def screenshot():
    counter = 0
    while True:
        #print(keyboard.read_key()) ###double checks if keyboard reading works
        #use 'p' to take screenshot
        if keyboard.read_key() == "p":
            #finds window that needs screenshot
            windowTop = gw.getWindowsWithTitle('top photosphere')[0]
            windowBottom = gw.getWindowsWithTitle('bottom photosphere')[0]
            windowMiddle = gw.getWindowsWithTitle('middle photosphere')[0]

            counter = counter + 1
            #takes screenshot, saves, and displays
            if windowTop and windowBottom and windowMiddle:
                frameTop = pyscreeze.screenshot(region=windowTop.box)
                #frameTop.show()
                #print(frameTop.size) #gets pizel size if the cam we use changes perchance
                topleft = 14
                toptop = 49
                topright = 794
                topbottom = 599
                frameTop = frameTop.crop((topleft, toptop, topright, topbottom))
                frameTop.save('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedTop' + str(counter) + '.png')
                #frameTop.show('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedTop' + str(counter) + '.png')
                print("showing")

                frameBottom = pyscreeze.screenshot(region=windowBottom.box)
                #frameBottom.show()
                #print(frameTop.size)
                bottomleft = 13
                bottomtop = 49
                bottomright = 802
                bottombottom = 596
                frameBottom = frameBottom.crop((bottomleft, bottomtop, bottomright, bottombottom))
                frameBottom.save('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedBottom' + str(counter) + '.png')
               # frameBottom.show('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedBottom' + str(counter) + '.png')
                print("showing")

                frameMiddle = pyscreeze.screenshot(region=windowMiddle.box)
                #frameBottom.show()
                #print(frameTop.size)
                middleleft = 13
                middletop = 49
                middleright = 802
                middlebottom = 596
                frameMiddle = frameMiddle.crop((bottomleft, bottomtop, bottomright, bottombottom))
                frameMiddle.save('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedBottom' + str(counter) + '.png')
               # frameBottom.show('C:/Users/SFHSR/OneDrive/Desktop/videoframes/savedBottom' + str(counter) + '.png')
                print("showing")

                print(counter)
                #frameBottom = pyscreeze.screenshot(region=windowBottom.box)
                #frameBottom.save('C:/Users/alyss/OneDrive/Desktop/videoframes/savedBottom.png')
                #frameBottom.show('C:/Users/alyss/OneDrive/Desktop/videoframes/savedBottom.png')

                pass

        if keyboard.read_key() == "q":
            break

#button to open cams
openButton = Button(displayTop, text = "open cams", command=new_window)
openButton.pack()

#threads screenshot function to run simultaneously with windows
screenshotThread = threading.Thread(target=screenshot, daemon=True)
screenshotThread.start()

#runs first window
displayTop.mainloop()