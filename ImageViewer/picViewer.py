#python 3!
from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title('ImageViewer')
root.iconbitmap("flock_ico01.ico")
frame = Frame(root, bg='light blue')
frame.grid(row=0, column=0, columnspan=3)

# variable to store which picture the program is at
imageIndexCounts = 0

#back and forward functions
def forward():
    global picLable
    global my_image
    global imageIndexCounts, buttonForward, status
    if imageIndexCounts == len(myImages)-1:
        buttonForward.configure(state='disabled', bg='purple', fg='white')
    if imageIndexCounts < len(myImages):
        picLable.grid_forget()
        imageIndexCounts+=1
        my_image = ImageTk.PhotoImage(Image.open(myImages[imageIndexCounts]))
        picLable = Label(frame, width=1500, height=800, image=my_image)
        picLable.grid(row=0, column=0, columnspan=3)
        buttonBackward.configure(state='active', bg='khaki', fg='white')
        status.grid_forget()
        status = Label(frame, text=" Image %d of %d" % (imageIndexCounts+1, len(myImages)), bd=1, relief='sunken', font='Akrobat 12 normal', bg='green')
        status.grid(row=1, column=4)


def back():
    global imageIndexCounts, picLable, my_image, buttonBackward, status
    if imageIndexCounts == 0:
        #buttonBack = Button(frame)
        buttonBackward.configure(state='disabled', bg='purple', fg='white')
    if imageIndexCounts > 0:
        picLable.grid_forget()
        imageIndexCounts-=1
        my_image = ImageTk.PhotoImage(Image.open(myImages[imageIndexCounts]))
        picLable = Label(frame, width=1500, height=800, image=my_image)
        picLable.grid(row=0, column=0, columnspan=3)
        buttonForward.configure(state='active', bg='khaki', fg='black')
        status.grid_forget()
        status = Label(frame, text=" Image %d of %d" % (imageIndexCounts+1, len(myImages)), bd=1, relief='sunken', font='Akrobat 12 normal', bg='green')
        status.grid(row=1, column=4)

#root.iconbitmap("Files_Web_File_Icon_256.png, "C:\Users\TAHIRUSALIFU\Pictures\Camera Roll\VIVP"")

#imageList
myImages = os.listdir(r'C:\Users\TAHIRUSALIFU\Pictures\Camera Roll\VIVP')

#change working directory to images directory
os.chdir(r'C:\Users\TAHIRUSALIFU\Pictures\Camera Roll\VIVP')

my_image = ImageTk.PhotoImage(Image.open(myImages[imageIndexCounts]))  #stores all image names in the directory

picLable = Label(frame, width=1500, height=800, image=my_image)
picLable.grid(row=0, column=0, columnspan=3)


#buttons: exit, forward, backward
buttonBackward = Button(frame, text="<<", command=back, bg='black', fg='white', width=18)
buttonForward = Button(frame, text=">>", command=forward, bg='black', fg='white', width=18)
exitButton = Button(frame, text='Exit Viewer', command=root.quit, bg='red', fg='white', width=32)

#status label
status = Label(frame, text=" Image %d of %d"% (imageIndexCounts+1, len(myImages)), bd=1, relief='sunken', font='Akrobat 12 normal', bg='green')
status.grid(row=1, column=4)

buttonBackward.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
buttonForward.grid(row=1, column=2)


root.mainloop()
