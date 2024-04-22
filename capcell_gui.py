import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox, filedialog # gives access to open/save files in home computer
from PIL import Image, ImageTk

# importing data inside each of the buttons 
def main():
    root = tk.Tk()
    root.title("Capcell Gen 3 Cell Imaging Platform")
    root.geometry("1000x800") # widthxheight in pixels 
    title_label = ttk.Label(root, text='Capcell Gen 3 Imaging') #creates label 
    title_label.grid(column=0, row=0)
    sample_label = ttk.Label(root, text='Image/Sample Name:')
    sample_label.grid(column=0, row=1, sticky=tk.W) # stick it to the east of the cell
    sample_entry = ttk.Entry(root)
    sample_data = tk.StringVar() # will need this in saving function later
    sample_entry.grid(column=1, row=1)



    # grid method creates things as large as they can be 
    root.mainloop() # shows window -- wait for user to do something (ie reason for main loop)

    # requires lots of playing around in order to see how it looks 

    # questions to fill screen? # to set window size and not change it 
    print("Finished") # prints to terminal window since it has been completed

if __name__ == "__main__":
    main()
