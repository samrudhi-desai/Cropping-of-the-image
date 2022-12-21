# Import the required libraries
import cv2 
import numpy as np
import glob
import os
from os import listdir
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from pathlib import Path
#from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
import time
import fnmatch
import tkinter.messagebox
# Create an instance of tkinter frame or window
win = Tk()
# Set the size of the window
win.geometry("350x350")
progress = Progressbar(win, orient=HORIZONTAL, length=100, mode='determinate')
class progress_bar(tk.Tk):
   def __init__(self):
       # tk.Tk.__init__(self)
        #self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        #self.progress.pack()
        self.val = 0
        self.maxval = 1
        #self.progress["maximum"] = 1

   def updating(self, val):
        self.val = val
        progress["value"] = val
        #win.update_idletasks()
        #print(self.val)

        if self.val == self.maxval:
            self.destroy()
   def create_subfolder():
         i=0
         source_path = filedialog.askdirectory(title='Select the Parent Directory')
   #result = Path(source_path).parent
   #print(result)
         site = os.path.basename(source_path)
         #print(site)
   #os.chdir(result)
         NewFolder = site+"_crop"
   #os.mkdir(NewFolder)
         path = os.path.join(source_path, NewFolder)
   #path = os.path.join(source_path, 'Images')
         os.makedirs(path)
         dir_list = fnmatch.filter(os.listdir(source_path), '*.tif')
         #dir_list = os.listdir(source_path)
         #print(dir_list)
         print("Files and directories in '", source_path, "' :")
#path= r"D:\test\Library St 3"
         counter= 0
         dir_list_length = len(dir_list)
         #print(dir_list_length)
         for file in dir_list:
               im= cv2.imread(source_path+"/"+file)
        #print(file)
        #print(im)
               if(im is not None):
                  gray1 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                  ret , thresh = cv2.threshold(gray1, 0, 255, 0)
                  contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                #print(file)
                  for c in contours:
                        (x,y,w,h) = cv2.boundingRect(c)
                        cv2.rectangle(im, (x,y), (x+w,y+h), (0,0,255))
                        roi = im[y:y+h, x:x+w]
                        #cv2.imwrite('AquaAI Images/15.12.11 32074-82077/15.12.11 32074-82077_seg7/s'+str(i)+'.jpg',roi)
                        cv2.imwrite(path+'\crop'+ str(i)+'.jpg',roi)
                        i= i+1
                        #print(i)
                        #print(file)
                        #cv2.waitKey()
                  counter= counter+1
                  #print("counter-" , counter)
                  percent = (counter/dir_list_length)*100
                  progress["value"] = percent
                  print(percent)
                  if percent == 100:
                     tkinter.messagebox.showinfo('Status of the cropping','The cropping of the selected folder has been completed')
                  win.update_idletasks()
                  time.sleep(1)
         cv2.destroyAllWindows()
         dir_ist = os.listdir(path)
         print(dir_ist)
         #global coun
         #coun = len(dir_ist)
         #print("Count of 'a' in array : ", elf.coun)
   progress.pack()      
   button1 = ttk.Button(win, text="Select a Folder", command=create_subfolder)
   button1.pack(pady=5)
   #win.after(10000,lambda:win.destroy())
   win.mainloop()
  
               
app = progress_bar()
#app.after(1, create_subfolder())
#progress.pack()
#percentLabel = Label(app, textvariable=percent).pack()
#mainloop()
   
