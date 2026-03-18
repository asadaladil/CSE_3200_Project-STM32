import tkinter as tk
from PIL import Image,ImageDraw,ImageOps
import numpy as np
from Prediction import predict_custom_matrix
from UART import UART
from train import Train
import time

CANVAS_SIZE=600       # Size of the window
MNIST_SIZE=28         # Target size (28x28)


def save(arr,y): # save for training
    for t in range(100):    
        with open(f"./Digit_Image_Array/Digit{y}.txt",mode="a") as file:
            for i in arr:
                for j in i:
                    file.write(f"{str(j)} ")
                file.write("\n")
            file.write(f"{str(y)}\n")

class DigitDrawer:
    def __init__(self,window):
        self.window=window
        self.digit=8
        self.window.title("STM32 Hand Written Digit Detection Interface")
        self.window.geometry(f'{CANVAS_SIZE}x{CANVAS_SIZE+60}+{500}+{50}') # center the interface

        self.writing_area=tk.Canvas(window, 
                                    width=CANVAS_SIZE, 
                                    height=CANVAS_SIZE, 
                                    bg='white')
        self.writing_area.pack(pady=10,padx=10)
        

        button=tk.Frame(window)
        button.pack()
        
        clear_button=tk.Button(button, 
                            text="Clear", 
                            command=self.clear_window, 
                            width=20,
                            bg="lightcoral")
        clear_button.pack(side=tk.LEFT,padx=20)
        
        submit_button=tk.Button(button, 
                                text="Detect", 
                                command=self.send_photo, 
                                width=20, 
                                bg="lightgreen")
        submit_button.pack(side=tk.LEFT,padx=20)
        
        wrong_button=tk.Button(button, 
                            text="Train", 
                            command=self.train, 
                            width=20,
                            bg="yellow")
        wrong_button.pack(side=tk.LEFT,padx=20)

        self.image = Image.new("L", 
                               (CANVAS_SIZE,CANVAS_SIZE), 
                               color=255)
        self.draw = ImageDraw.Draw(self.image)

        self.writing_area.bind("<B1-Motion>", self.paint) # Bind Mouse Events
        

    def paint(self,event):
        brush=20
        x1,y1=(event.x-brush),(event.y-brush)
        x2,y2=(event.x+brush),(event.y+brush)
        
        self.writing_area.create_oval(x1,y1,x2,y2,fill='black',width=0) #screen draw
        
        self.draw.ellipse([x1,y1,x2,y2],fill=0) # Draw on the memory image (For processing)

    def clear_window(self):
        self.writing_area.delete("all")
        self.image=Image.new("L", 
                            (CANVAS_SIZE,CANVAS_SIZE), 
                            color=255)
        self.draw=ImageDraw.Draw(self.image)

    def send_photo(self):
        x=time.time()*1000
        # 1. Resize to 28x28 (Standard MNIST size)
        temp=self.image.resize((MNIST_SIZE, MNIST_SIZE),Image.Resampling.LANCZOS)
        
        # 2. Invert colors (MNIST is White text on Black background)
        digit_image_array = ImageOps.invert(temp) 
        
        # 3. Convert to Numpy Array (28x28 matrix)
        digit_image_array=np.array(digit_image_array)
        self.digit=predict_custom_matrix(digit_image_array)
        
        # save(digit_image_array)
        z=time.time()*1000
        UART(self.digit)
        y=time.time()*1000
        print(f"{np.round((y-x),2)} {np.round(y-z,2)}")
    
    def train(self):
        img=self.image.resize((MNIST_SIZE, MNIST_SIZE),Image.Resampling.LANCZOS)
        digit_image_array = ImageOps.invert(img)
        digit_image_array=np.array(digit_image_array)
        y=Train(self.window)
        if y!=None:
            save(digit_image_array,y)
        


