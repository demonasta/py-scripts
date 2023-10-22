import os 
from PIL import Image 
import tkinter 
from tkinter import simpledialog


Square_fit = simpledialog.askinteger("Image Size", "Enter the image size:")
New_folder = simpledialog.askstring("Folder Name", "Enter the folder name:")

os.makedirs(New_folder, exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')):
        continue 

    im = Image.open(filename)
    width , height = im.size

    if width > Square_fit and height > Square_fit:
        if width > height:
            height = int((Square_fit/width)*height)
            width = Square_fit
        else :
            width = int((Square_fit/height)*width)
            height = Square_fit
        
        print('Resizing ' %(filename))
        im = im.resize((width, height))

    
    im.save(os.path.join(New_folder , filename))

print('Done Resizing all images ... :] ')
        
